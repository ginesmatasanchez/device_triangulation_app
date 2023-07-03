```mermaid
erDiagram
    Usuario {
        Int id_usuario PK
        String nombre
        String clave
        String email
        Int id_empresa
        Int id_perfil
        String movil
        Date creado
        Date ultimologin
        Int activo
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
        String nif
        String direccion
        String cp
        String poblacion
        String provincia
        String pais
        String registro
        String telefono
        String movil
        String email
        String web
        Timestamp creado
        Int activo
    }

    Usuario ||--o{ Administrador : pertenece_a
    Administrador ||--o{ Edificio : es_propietario_de
    Edificio ||--|{ Planta : contiene
    Edificio ||--o{ Empresa : pertenece_a
    Dispositivo ||--o{ Punto : tiene
    Triangulo ||--o{ Punto : tiene
    Zona ||--o{ Triangulo : contiene
    Planta ||--|{ Zona : contiene
    Usuario ||--o{ Empresa : pertenece_a
