import pytest
from flask import g
from flask import session

from flaskr.db import get_db


def test_register(client, app):
    # test that viewing the page renders without template errors
    assert client.get("/auth/register").status_code == 200

    # test that successful registration redirects to the login page
    response = client.post("/auth/register", data={"username": "a", "password": "a1234567"})
    assert response.headers["Location"] == "/auth/login"

    # test that the user was inserted into the database
    with app.app_context():
        assert (
            get_db().execute("SELECT * FROM user WHERE username = 'a'").fetchone()
            is not None
        )


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (
        ("", "", b"Username is required."),
        ("a", "", b"Password is required."),
        ("test", "test1234", b"already registered"),
    ),
)
def test_register_validate_input(client, username, password, message):
    response = client.post(
        "/auth/register", data={"username": username, "password": password}
    )
    assert message in response.data


def test_login(client, auth):
    # test that viewing the page renders without template errors
    assert client.get("/auth/login").status_code == 200

    # test that successful login redirects to the index page
    response = auth.login()
    assert response.headers["Location"] == "/"

    # login request set the user_id in the session
    # check that the user is loaded from the session
    with client:
        client.get("/")
        assert session["user_id"] == 1
        assert g.user["username"] == "test"


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (("a", "test", b"Incorrect username."), ("test", "a", b"Incorrect password.")),
)
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert "user_id" not in session



@pytest.mark.parametrize(
    ("username", "password", "valid"),
    (
        ("nuevo1", "1234567", False),       # 7 caracteres: debe rechazar
        ("nuevo2", "12345678", True),       # 8 caracteres: debe aceptar
        ("nuevo3", "a", False),             # 1 caracter: debe rechazar
        ("nuevo4", "123456789012", True),   # 12 caracteres: debe aceptar
    ),
)
def test_register_password_length(client, app, username, password, valid):
    # Enviamos el formulario de registro con el usuario y contraseña del caso
    response = client.post(
        "/auth/register", data={"username": username, "password": password}
    )

    # Buscamos en la base de datos si el usuario se ha creado
    with app.app_context():
        user = (
            get_db()
            .execute("SELECT * FROM user WHERE username = ?", (username,))
            .fetchone()
        )

    if valid:
        # Contraseña correcta: nos lleva al login y el usuario existe
        assert response.headers["Location"] == "/auth/login"
        assert user is not None
    else:
        # Contraseña corta: sale el mensaje de error y el usuario NO existe
        assert b"at least 8 characters" in response.data
        assert user is None