from Repositories import TareaRepository, EstadoRepository, UsuarioRepository
from Classes import Tarea
from datetime import datetime
 
 
class TareaService:
    def __init__(self):
        self.repo = TareaRepository()
 
    # READ 
    def obtener_por_id(self, id_tarea: int):
        tarea = self.repo.obtener_por_id(id_tarea)
        if not tarea:
            return None
        return self._serializar(tarea)
    def obtener_todos(self, id_estado: int):
        tareas = self.repo.obtener_todos(id_estado)
        return [self._serializar(t) for t in tareas]
 
    # CREATE 
    def crear(self, titulo: str, descripcion: str, prioridad: int,
              id_estado: int, fecha_vencimiento, id_usuario_asignado: int,  posicion: int):
        repo_estado = EstadoRepository()
        estado = repo_estado.obtener_por_id(id_estado)
        if not estado:
            return False, f"Estado {id_estado} no encontrado"

        repo_usuario = UsuarioRepository()
        usuario = repo_usuario.obtener_por_id(id_usuario_asignado)
        if not usuario:
            return False, f"Usuario {id_usuario_asignado} no encontrado"

        nueva = Tarea(
            id=None,
            fechaCreacion=datetime.now(),
            fechaModificacion=datetime.now(),
            titulo=titulo,
            descripcion=descripcion,
            prioridad=prioridad,
            estado=estado,
            usuarioAsignado=usuario, 
            fechaVencimiento=fecha_vencimiento,
            posicion=posicion,
            comentarios=[]
        )
        self.repo.crear(nueva)
        return True, None
 
    # UPDATE - Datos generales
    def actualizar_datos(self, id_tarea: int, titulo: str, descripcion: str,
                         prioridad: int, fecha_vencimiento, posicion: int):
        tarea = self.repo.obtener_por_id(id_tarea)
        if not tarea:
            return False
        tarea.titulo = titulo
        tarea.descripcion = descripcion
        tarea.prioridad = prioridad
        tarea.fechaVencimiento = fecha_vencimiento
        tarea.posicion = posicion
        self.repo.actualizar(tarea)
        return True
 
    # UPDATE - mover a otro estado 
    def mover_estado(self, id_tarea: int, id_estado_nuevo: int):
        tarea = self.repo.obtener_por_id(id_tarea)
        if not tarea:
            return False, f"Tarea {id_tarea} no encontrada"
 
        repo_estado = EstadoRepository()
        estado_nuevo = repo_estado.obtener_por_id(id_estado_nuevo)
        if not estado_nuevo:
            return False, f"Estado {id_estado_nuevo} no encontrado"
 
        tarea.cambiar_estado(estado_nuevo)
        self.repo.actualizar(tarea)
        return True, None
 
    # UPDATE - asignar usuario 
    def asignar_usuario(self, id_tarea: int, id_usuario: int):
        tarea = self.repo.obtener_por_id(id_tarea)
        if not tarea:
            return False, f"Tarea {id_tarea} no encontrada"
 
        repo_usuario = UsuarioRepository()
        usuario = repo_usuario.obtener_por_id(id_usuario)
        if not usuario:
            return False, f"Usuario {id_usuario} no encontrado"
 
        tarea.asignar_usuario(usuario)
        self.repo.actualizar(tarea)
        return True, None
 
    # DELETE 
    def eliminar(self, id_tarea: int):
        tarea = self.repo.obtener_por_id(id_tarea)
        if not tarea:
            return False
        self.repo.eliminar(id_tarea)
        return True
 
    # Serialización 
    def _serializar(self, tarea) -> dict:
        return {
            "id": tarea.id,
            "titulo": tarea.titulo,
            "descripcion": tarea.descripcion,
            "prioridad": tarea.prioridad,
            "usuario_asignado_id": tarea.usuarioAsignado.id,
            "estado_id": tarea.estado.id,
            "fecha_vencimiento": str(tarea.fechaVencimiento),
            "posicion": tarea.posicion,
            "fecha_creacion": str(tarea.fechaCreacion),
            "fecha_modificacion": str(tarea.fechaModificacion),
        }