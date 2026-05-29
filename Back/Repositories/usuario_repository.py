from Classes.usuario import Usuario
from .db_connection import get_connection
from datetime import datetime

class UsuarioRepository:

    # CREATE
    def crear(self, usuario):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO usuario
        (nombre, apellido, mail, contrasena, activo, fecha_creacion, fecha_modificacion)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(
            query,
            usuario.nombre,
            usuario.apellido,
            usuario.mail,
            usuario.contrasena,
            usuario.activo,
            usuario.fechaCreacion,
            usuario.fechaModificacion
        )
        conn.commit()
        conn.close()

    # READ BY ID
    def obtener_por_id(self, id_usuario):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM usuario WHERE id = ?"
        cursor.execute(query, id_usuario)
        row = cursor.fetchone()
        conn.close()
        if row:
            return Usuario(
                row.id,
                row.fecha_creacion,
                row.fecha_modificacion,
                row.nombre,
                row.apellido,
                row.mail,
                row.contrasena,
                [],  # tableros
                row.activo
            )
        return None
    
    # READ BY MAIL
    def obtener_por_mail(self, mail_usuario):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM usuario WHERE mail = ?"
        cursor.execute(query, mail_usuario)
        row = cursor.fetchone()
        conn.close()
        if row:
            return Usuario(
                row.id,
                row.fecha_creacion,
                row.fecha_modificacion,
                row.nombre,
                row.apellido,
                row.mail,
                row.contrasena,
                [],  # tableros
                row.activo
            )
        return None

    # READ ALL
    def obtener_todos(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM usuario"
        cursor.execute(query)
        rows = cursor.fetchall()
        usuarios = []
        for row in rows:
            usuario = Usuario(
                row.id,
                row.fecha_creacion,
                row.fecha_modificacion,
                row.nombre,
                row.apellido,
                row.mail,
                row.contrasena,
                [],
                row.activo
            )
            usuarios.append(usuario)
        conn.close()
        return usuarios

    # UPDATE
    def actualizar(self, usuario):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE usuario
        SET nombre = ?,
            apellido = ?,
            mail = ?,
            contrasena = ?,
            activo = ?,
            fecha_modificacion = ?
        WHERE id = ?
        """
        cursor.execute(
            query,
            usuario.nombre,
            usuario.apellido,
            usuario.mail,
            usuario.contrasena,
            usuario.activo,
            datetime.now(),
            usuario.id
        )
        conn.commit()
        conn.close()

    # DELETE
    def eliminar(self, id_usuario):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM usuario WHERE id = ?"
        cursor.execute(query, id_usuario)
        conn.commit()
        conn.close()
