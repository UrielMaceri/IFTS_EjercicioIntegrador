CREATE DATABASE EjercicioIntegrador;
USE EjercicioIntegrador;

-- =========================
-- USUARIO
-- =========================
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100),
    mail VARCHAR(150) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion DATETIME,
    fecha_modificacion DATETIME
);

-- =========================
-- TABLERO
-- =========================
CREATE TABLE tablero (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    propietario_id INT,
    fecha_creacion DATETIME,
    fecha_modificacion DATETIME,
    FOREIGN KEY (propietario_id) REFERENCES usuario(id)
        ON DELETE CASCADE
);

-- =========================
-- ESTADO (columnas)
-- =========================
CREATE TABLE estado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    posicion INT,
    tablero_id INT,
    fecha_creacion DATETIME,
    fecha_modificacion DATETIME,
    FOREIGN KEY (tablero_id) REFERENCES tablero(id)
        ON DELETE CASCADE
);

-- =========================
-- TAREA
-- =========================
CREATE TABLE tarea (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT,
    prioridad INT,
    usuario_asignado_id INT,
    estado_id INT,
    fecha_vencimiento DATETIME,
    posicion INT,
    fecha_creacion DATETIME,
    fecha_modificacion DATETIME,
    
    FOREIGN KEY (usuario_asignado_id) REFERENCES usuario(id)
        ON DELETE SET NULL,

    FOREIGN KEY (estado_id) REFERENCES estado(id)
        ON DELETE CASCADE
);

-- =========================
-- COMENTARIO
-- =========================
CREATE TABLE comentario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tarea_id INT,
    usuario_id INT,
    contenido TEXT,
    usuario_mod INT,
    fecha_creacion DATETIME,
    fecha_modificacion DATETIME,

    FOREIGN KEY (tarea_id) REFERENCES tarea(id)
        ON DELETE CASCADE,

    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        ON DELETE CASCADE,

    FOREIGN KEY (usuario_mod) REFERENCES usuario(id)
        ON DELETE SET NULL
);