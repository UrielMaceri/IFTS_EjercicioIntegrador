from Classes.tablero import Tablero
from Repositories.usuario_repository import UsuarioRepository
from .db_connection import get_connection
from datetime import datetime


class TableroRepository:

    def __init__(self):
        self.usuario_repo = UsuarioRepository()

    # Insert
    def crear(self, tablero):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO tablero
        (nombre, descripcion, propietario_id, fecha_creacion, fecha_modificacion)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(
            query,
            tablero.nombre,
            tablero.descripcion,
            tablero.propietario.id,   # FK
            tablero.fechaCreacion,
            tablero.fechaModificacion
        )
        conn.commit()
        conn.close()

    # READ BY ID
    def obtener_por_id(self, id_tablero):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM tablero WHERE id = ?"
        cursor.execute(query, id_tablero)
        row = cursor.fetchone()
        conn.close()
        if row:
            propietario = self.usuario_repo.obtener_por_id(
                row.propietario_id
            )
            return Tablero(
                row.id,
                row.fecha_creacion,
                row.fecha_modificacion,
                row.nombre,
                row.descripcion,
                [],
                propietario
            )
        return None

    # READ ALL
    def obtener_todos(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM tablero"
        cursor.execute(query)
        rows = cursor.fetchall()
        tableros = []
        for row in rows:
            propietario = self.usuario_repo.obtener_por_id(
                row.propietario_id
            )
            tablero = Tablero(
                row.id,
                row.fecha_creacion,
                row.fecha_modificacion,
                row.nombre,
                row.descripcion,
                [],
                propietario
            )
            tableros.append(tablero)
        conn.close()
        return tableros

    # UPDATE
    def actualizar(self, tablero):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE tablero
        SET nombre = ?,
            descripcion = ?,
            propietario_id = ?,
            fecha_modificacion = ?
        WHERE id = ?
        """
        cursor.execute(
            query,
            tablero.nombre,
            tablero.descripcion,
            tablero.propietario.id,
            datetime.now(),
            tablero.id
        )
        conn.commit()
        conn.close()

    # DELETE
    def eliminar(self, id_tablero):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM tablero WHERE id = ?"
        cursor.execute(query, id_tablero)
        conn.commit()
        conn.close()