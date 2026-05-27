from Repositories import ComentarioRepository, TareaRepository, UsuarioRepository
from Classes import Comentario
from datetime import datetime
 
 
class ComentarioService:
    def __init__(self):
        self.repo = ComentarioRepository()
 
    # READ 
    def obtener_por_id(self, id_comentario: int):
        comentario = self.repo.obtener_por_id(id_comentario)
        if not comentario:
            return None
        return self._serializar(comentario)
    def obtener_todos(self, id_tarea: int):
        comentarios = self.repo.obtener_todos(id_tarea)
        return [self._serializar(c) for c in comentarios]
 
    # CREATE 
    def crear(self, id_tarea: int, id_usuario: int, contenido: str):
        repo_tarea = TareaRepository()
        tarea = repo_tarea.obtener_por_id(id_tarea)
        if not tarea:
            return False, f"Tarea {id_tarea} no encontrada"
 
        repo_usuario = UsuarioRepository()
        usuario = repo_usuario.obtener_por_id(id_usuario)
        if not usuario:
            return False, f"Usuario {id_usuario} no encontrado"
 
        nuevo = Comentario(
            id=None,
            fechaCreacion=datetime.now(),
            fechaModificacion=datetime.now(),
            tarea=tarea,
            usuario=usuario,
            contenido=contenido,
            usuarioMod=usuario   # al crear, el autor y el modificador son el mismo
        )
        self.repo.crear(nuevo)
        return True, None
 
    # UPDATE 
    def actualizar_contenido(self, id_comentario: int, contenido: str, id_usuario_mod: int):
        comentario = self.repo.obtener_por_id(id_comentario)
        if not comentario:
            return False, f"Comentario {id_comentario} no encontrado"
 
        repo_usuario = UsuarioRepository()
        usuario_mod = repo_usuario.obtener_por_id(id_usuario_mod)
        if not usuario_mod:
            return False, f"Usuario {id_usuario_mod} no encontrado"
 
        comentario.contenido = contenido
        comentario.usuarioMod = usuario_mod
        self.repo.actualizar(comentario)
        return True, None
 
    # DELETE 
    def eliminar(self, id_comentario: int):
        comentario = self.repo.obtener_por_id(id_comentario)
        if not comentario:
            return False
        self.repo.eliminar(id_comentario)
        return True
 
    # Serialización 
    def _serializar(self, comentario) -> dict:
        return {
            "id": comentario.id,
            "tarea_id": comentario.tarea.id,
            "usuario_id": comentario.usuario.id,
            "contenido": comentario.contenido,
            "usuario_mod_id": comentario.usuarioMod.id,
            "fecha_creacion": str(comentario.fechaCreacion),
            "fecha_modificacion": str(comentario.fechaModificacion),
        }