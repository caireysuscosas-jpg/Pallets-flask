# Diagrama de clases

## Objetivo
Este archivo muestra con un dibujo cómo se guardan los datos de la aplicación. Hay dos partes: usuarios (USER) y publicaciones (POST). Un usuario puede escribir muchas publicaciones.

```mermaid
classDiagram
    class USER {
        +INTEGER id PK
        +TEXT username UNIQUE
        +TEXT password
    }

    class POST {
        +INTEGER id PK
        +INTEGER author_id FK
        +TIMESTAMP created
        +TEXT title
        +TEXT body
    }

    USER "1" --> "0..*" POST : escribe
```