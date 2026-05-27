from Classes.comentario import Comentario
from Repositories.usuario_repository import UsuarioRepository
from Repositories.tarea_repository import TareaRepository
from .db_connection import get_connection
from datetime import datetime

class ComentarioRepository:

    def __init__(self):
        self.tarea_repo = TareaRepository()
        self.usuario_repo = UsuarioRepository()

        # Insert
    def crear(self, comentario):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO comentario
        (tarea_id, usuario_id, contenido, usuario_mod, fecha_creacion, fecha_modificacion)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(
            query,
            comentario.tarea.id,
            comentario.usuario.id,
            comentario.contenido,
            comentario.usuarioMod.id,
            comentario.fechaCreacion,
            comentario.fechaModificacion
        )
        conn.commit()
        conn.close()

    # READ BY ID
    def obtener_por_id(self, id_comentario):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM comentario WHERE id = ?"
        cursor.execute(query, id_comentario)
        row = cursor.fetchone()
        conn.close()
        if row:
            usuario = self.usuario_repo.obtener_por_id(row.usuario_id)
            usuarioMod = self.usuario_repo.obtener_por_id(row.usuario_mod)
            tarea = self.tarea_repo.obtener_por_id(row.tarea_id)
            return Comentario(
                row.id,
                row.fecha_creacion,
                row.fecha_modificacion,
                tarea,
                usuario,
                row.contenido,
                usuarioMod
            )
        return None
    
    # READ ALL
    def obtener_todos(self, id_tareas):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM comentario wherr tarea_id = ?"
        cursor.execute(query, id_tareas)
        rows = cursor.fetchall()
        comentarios = []
        for row in rows:
            usuario = self.usuario_repo.obtener_por_id(row.usuario_id)
            tarea = self.tarea_repo.obtener_por_id(row.tarea_id)
            comentario = Comentario(
                row.id,
                row.fecha_creacion,
                row.fecha_modificacion,
                tarea,
                usuario,
                row.contenido,
                row.usuario_mod
            )
            comentarios.append(comentario)
        conn.close()
        return comentarios
    
    # UPDATE
    def actualizar(self, comentario):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE comentario
        SET contenido = ?,
            fecha_modificacion = ?
        WHERE id = ?
        """
        cursor.execute(
            query,
            comentario.contenido,
            datetime.now(),
            comentario.id
        )
        conn.commit()
        conn.close()

    # DELETE
    def eliminar(self, id_comentario):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM comentario WHERE id = ?"
        cursor.execute(query, id_comentario)
        conn.commit()
        conn.close()