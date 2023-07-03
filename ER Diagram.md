````mermaid
erDiagram
    User {
        Int id_usuario PK
        String email
        String contrasena
    }

    Administrador {
        Int id_administrador PK
    }

    Edificio {
        Int id_edificio PK
        String nombre
        Decimal latitud
        Decimal longitud
    }

    Planta {
        Int id_planta PK
        Int numero_planta
    }

    Dispositivo {
        Int id_dispositivo PK
        String tipo_dispositivo
        Int nivel_bateria
    }

    Punto {
        Int id_punto PK
        Float x
        Float y
        Float z
    }

    Triangulo {
        Int id_triangulo PK
    }

    Zona {
        Int id_zona PK
        String nombre
        Int posicion_triangulo
    }

    Empresa {
        Int id_empresa PK
        String nombre
        String direccion
        String telefono
        String email
        Timestamp creado
        Int activo
    }

    User ||--o{ Administrador : belongs_to
    Administrador ||--o{ Edificio : owns
    Edificio ||--|{ Planta : contains
    Edificio ||--o{ Empresa : belongs_to
    Dispositivo ||--o{ Punto : has
    Triangulo ||--o{ Punto : has
    Zona ||--o{ Triangulo : contains
    Planta ||--|{ Zona : contains
    User ||--o{ Empresa : belongs_to

´´´
