from Classes.estado import Estado
from Repositories.tablero_repository import TableroRepository
from .db_connection import get_connection
from datetime import datetime

class EstadoRepository:

    def __init__(self):
        self.tablero_repo = TableroRepository()

    # Insert
    def crear(self, estado):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO estado
        (nombre, posicion, tablero_id, fecha_creacion, fecha_modificacion)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(
            query,
            estado.nombre,
            estado.posicion,
            estado.tablero.id,
            estado.fechaCreacion,
            estado.fechaModificacion
        )
        conn.commit()
        conn.close()

    # READ BY ID
    def obtener_por_id(self, id_estado):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM estado WHERE id = ?"
        cursor.execute(query, id_estado)
        row = cursor.fetchone()
        conn.close()
        if row:
            tablero = self.tablero_repo.obtener_por_id(row.tablero_id)
            return Estado(
                row.id,
                row.fecha_creacion,
                row.fecha_modificacion,
                row.nombre,
                row.posicion,
                tablero,
                []
            )
        return None
    
    # READ ALL
    def obtener_todos(self, id_tablero):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM estado where tablero_id = ?"
        cursor.execute(query, id_tablero)
        rows = cursor.fetchall()
        estados = []
        for row in rows:
            tablero = self.tablero_repo.obtener_por_id(row.tablero_id)
            estado = Estado(
                    row.id,
                    row.fecha_creacion,
                    row.fecha_modificacion,
                    row.nombre,
                    row.posicion,
                    tablero,
                    []
                )
            estados.append(estado)
        conn.close()
        return estados

    # UPDATE
    def actualizar(self, estado):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE estado
        SET nombre = ?,
            posicion = ?,
            tablero_id = ?,
            fecha_modificacion = ?
        WHERE id = ?
        """
        cursor.execute(
            query,
            estado.nombre,
            estado.posicion,
            estado.tablero.id,
            datetime.now(),
            estado.id
        )
        conn.commit()
        conn.close()

    # DELETE
    def eliminar(self, id_estado):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM estado WHERE id = ?"
        cursor.execute(query, id_estado)
        conn.commit()
        conn.close()