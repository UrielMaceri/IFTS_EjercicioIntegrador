CREATE DATABASE EjercicioIntegrador;
GO

USE EjercicioIntegrador;
GO

-- =========================
-- USUARIO
-- =========================
CREATE TABLE usuario (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    apellido NVARCHAR(100),
    mail NVARCHAR(150) UNIQUE NOT NULL,
    contrasena NVARCHAR(255) NOT NULL,
    activo BIT DEFAULT 1,
    fecha_creacion DATETIME,
    fecha_modificacion DATETIME
);

-- =========================
-- TABLERO
-- =========================
CREATE TABLE tablero (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    descripcion NVARCHAR(MAX),
    propietario_id INT,
    fecha_creacion DATETIME,
    fecha_modificacion DATETIME,

    CONSTRAINT FK_tablero_usuario
        FOREIGN KEY (propietario_id)
        REFERENCES usuario(id)
        ON DELETE CASCADE
);

-- =========================
-- ESTADO (columnas)
-- =========================
CREATE TABLE estado (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    posicion INT,
    tablero_id INT,
    fecha_creacion DATETIME,
    fecha_modificacion DATETIME,

    CONSTRAINT FK_estado_tablero
        FOREIGN KEY (tablero_id)
        REFERENCES tablero(id)
        ON DELETE CASCADE
);

-- =========================
-- TAREA
-- =========================
CREATE TABLE tarea (
    id INT IDENTITY(1,1) PRIMARY KEY,
    titulo NVARCHAR(150) NOT NULL,
    descripcion NVARCHAR(MAX),
    prioridad INT,
    usuario_asignado_id INT,
    estado_id INT,
    fecha_vencimiento DATETIME,
    posicion INT,
    fecha_creacion DATETIME,
    fecha_modificacion DATETIME,

    CONSTRAINT FK_tarea_usuario
        FOREIGN KEY (usuario_asignado_id)
        REFERENCES usuario(id),

    CONSTRAINT FK_tarea_estado
        FOREIGN KEY (estado_id)
        REFERENCES estado(id)
        ON DELETE CASCADE
);

-- =========================
-- COMENTARIO
-- =========================
CREATE TABLE comentario (
    id INT IDENTITY(1,1) PRIMARY KEY,
    tarea_id INT,
    usuario_id INT,
    contenido NVARCHAR(MAX),
    usuario_mod INT,
    fecha_creacion DATETIME,
    fecha_modificacion DATETIME,

    CONSTRAINT FK_comentario_tarea
        FOREIGN KEY (tarea_id)
        REFERENCES tarea(id)
        ON DELETE CASCADE,

    CONSTRAINT FK_comentario_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuario(id),

    CONSTRAINT FK_comentario_usuario_mod
        FOREIGN KEY (usuario_mod)
        REFERENCES usuario(id)
);