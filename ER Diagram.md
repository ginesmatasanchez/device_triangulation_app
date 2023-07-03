erDiagram
    entity "Usuario" as usuario {
        id_usuario INT <<PK>>
        email VARCHAR(255)
        contraseña VARCHAR(255)
    }

    entity "Administrador" as administrador {
        id_administrador INT <<PK>>
    }

    entity "Edificio" as edificio {
        id_edificio INT <<PK>>
        nombre VARCHAR(255)
        latitud DECIMAL(10, 6)
        longitud DECIMAL(10, 6)
    }

    entity "Planta" as planta {
        id_planta INT <<PK>>
        numero_planta INT
    }

    entity "Dispositivo" as dispositivo {
        id_dispositivo INT <<PK>>
        tipo_dispositivo VARCHAR(255)
        nivel_bateria INT
    }

    entity "Punto" as punto {
        id_punto INT <<PK>>
        x FLOAT
        y FLOAT
        z FLOAT
    }

    entity "Triangulo" as triangulo {
        id_triangulo INT <<PK>>
    }

    entity "Zona" as zona {
        id_zona INT <<PK>>
        nombre VARCHAR(255)
        posicion_triangulo INT
    }

    entity "Empresa" as empresa {
        id_empresa INT <<PK>>
        nombre VARCHAR(50)
        direccion VARCHAR(100)
        telefono VARCHAR(20)
        email VARCHAR(50)
        creado TIMESTAMP
        activo INT
    }

    usuario ||--|{ administrador : belongs to
    administrador ||--o{ edificio : owns
    edificio ||--|{ planta : contains
    edificio ||--o{ empresa : belongs to
    dispositivo ||--o{ punto : has
    triangulo ||--o{ punto : has
    zona ||--o{ triangulo : contains
    planta ||--|{ zona : contains
    usuario ||--o{ empresa : belongs to
