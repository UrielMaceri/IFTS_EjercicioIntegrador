from Classes.tarea import Tarea
from Repositories.usuario_repository import UsuarioRepository
from Repositories.estado_repository import EstadoRepository
from .db_connection import get_connection
from datetime import datetime

class TareaRepository:

    def __init__(self):
        self.estado_repo = EstadoRepository()
        self.usuario_repo = UsuarioRepository()

    # Insert
    def crear(self, tarea):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO tarea
        (titulo, descripcion, prioridad, usuario_asignado_id, estado_id, fecha_vencimiento, posicion, fecha_creacion, fecha_modificacion)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(
            query,
            tarea.titulo,
            tarea.descripcion,
            tarea.prioridad,
            tarea.usuarioAsignado.id,
            tarea.estado.id,
            tarea.fechaVencimiento,
            tarea.posicion,
            tarea.fechaCreacion,
            tarea.fechaModificacion
        )
        conn.commit()
        conn.close()

    # READ BY ID
    def obtener_por_id(self, id_tarea):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM tarea WHERE id = ?"
        cursor.execute(query, id_tarea)
        row = cursor.fetchone()
        conn.close()
        if row:
            usuario = self.usuario_repo.obtener_por_id(row.usuario_asignado_id)
            estado = self.estado_repo.obtener_por_id(row.estado_id)
            return Tarea(
                row.id,
                row.fecha_creacion,
                row.fecha_modificacion,
                row.titulo,
                row.descripcion,
                row.prioridad,
                estado,
                usuario,
                row.fecha_vencimiento,
                row.posicion,            
                []
            )
        return None
    
    # READ ALL
    def obtener_todos(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM tarea"
        cursor.execute(query)
        rows = cursor.fetchall()
        tareas = []
        for row in rows:
            usuario = self.usuario_repo.obtener_por_id(row.usuario_asignado_id)
            estado = self.estado_repo.obtener_por_id(row.estado_id)
            tarea = Tarea(
                row.id,
                row.fecha_creacion,
                row.fecha_modificacion,
                row.titulo,
                row.descripcion,
                row.prioridad,
                estado,
                usuario,
                row.fecha_vencimiento,
                row.posicion,            
                []
            )
            tareas.append(tarea)
        conn.close()
        return tareas
    
    # UPDATE
    def actualizar(self, tarea):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE tarea
        SET titulo = ?,
            descripcion = ?,
            prioridad = ?,
            usuario_asignado_id = ?,
            estado_id = ?,
            fecha_vencimiento = ?,
            posicion = ?,
            fecha_modificacion = ?
        WHERE id = ?
        """
        cursor.execute(
            query,
            tarea.titulo,
            tarea.descripcion,
            tarea.prioridad,
            tarea.usuarioAsignado.id,
            tarea.estado.id,
            tarea.fechaVencimiento,
            tarea.posicion,
            datetime.now(),
            tarea.id
        )
        conn.commit()
        conn.close()

    # DELETE
    def eliminar(self, id_tarea):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM tarea WHERE id = ?"
        cursor.execute(query, id_tarea)
        conn.commit()
        conn.close()