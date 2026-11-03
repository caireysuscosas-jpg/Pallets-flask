# Documentació de Diagrames UML

Aquest repositori conté la documentació visual dels diagrames de seqüència UML del sistema. Tots aquests diagrames estan recollits al document PDF situat a la carpeta diagrams.

---

## Enllaç al Document
[Veure el PDF complet amb els Diagrames UML](./diagrams/Diagramas%20UML%20.pdf)

---

## Descripció dels Diagrames

### 1. Happy Path General (Tot correcte)
* **Captura:** Procés d'inici de sessió general exitós.
* **Descripció:** L'usuari accedeix al formulari i envia les seves credencials. El servei d'autenticació consulta la base de dades, valida les dades i confirma que les credencials són correctes, iniciant la sessió satisfactòriament.

---

### 2. Escenaris Alternatius Generals

#### 2.1 Login (Credencials invàlides)
* **Captura:** Intent d'accés amb dades d'usuari incorrectes.
* **Descripció:** L'usuari envia un nom d'usuari o contrasenya erronis. La base de dades no troba la coincidència, el servei valida l'error i retorna un missatge a la interfície per indicar que les credencials són invàlides. La sessió no s'inicia.

#### 2.2 Sistema no accessible (Servidor / Base de dades)
* **Captura:** Caiguda o falta de resposta del servidor o la base de dades.
* **Descripció:** Quan la interfície envia les credencials però la base de dades no respon, el servei captura la fallada i mostra un missatge d'error general de sistema a l'usuari.

#### 2.3 Format del correu incorrecte
* **Captura:** Validació de format al client.
* **Descripció:** Si l'usuari escriu un correu sense el format vàlid, la interfície web atura el procés immediatament i mostra un error de format sense arribar a enviar res al servidor.

---

### 3. Login Correcte (Happy Path Detallat)
* **Captura:** Flux detallat d'autenticació.
* **Descripció:** Mostra els passos exactes:
  1. Carregar el formulari d'accés.
  2. Enviar les dades des del formulari.
  3. Comprovació de la contrasenya i desat de la sessió.
  4. Redirecció a la pàgina principal mostrant la sessió iniciada.

---

### 4. Fluxes Alternatius Detallats de Login

#### 4.1 Escenari 1: Credencials invàlides (Detallat)
* **Captura:** Procés en fallada de credencials.
* **Descripció:** Es realitza l'enviament de dades, es comprova la contrasenya a la base de dades i, en no coincidir, es gestiona la resposta d'error mantenint l'usuari a la pantalla d'accés.

#### 4.2 Escenari 2: Sistema no accessible (Detallat)
* **Captura:** Gestió d'errors de connexió en la petició d'accés.
* **Descripció:** Després d'enviar les dades, es produeix un error de connexió amb la base de dades. El servei gestiona la fallada i mostra un missatge d'error a la interfície.
