from Repositories import UsuarioRepository
from Classes import Usuario
from datetime import datetime
 
class UsuarioService:
    def __init__(self):
        self.repo = UsuarioRepository()
 
    # READ
    def obtener_por_id(self, id_usuario: int):
        usuario = self.repo.obtener_por_id(id_usuario)
        if not usuario:
            return None
        return self._serializar(usuario)
    def obtener_todos(self):
        usuarios = self.repo.obtener_todos()
        return [self._serializar(u) for u in usuarios]

    # CREATE
    def crear(self, nombre: str, apellido: str, mail: str, contrasena: str):
        nuevo = Usuario(
            id=None,
            fechaCreacion=datetime.now(),
            fechaModificacion=datetime.now(),
            nombre=nombre,
            apellido=apellido,
            mail=mail,
            contraseña=contrasena,
            tableros=[],
            activo=True
        )
        self.repo.crear(nuevo)
    
    # UPDATE - SOLO datos generales, no contraseña
    def actualizar_datos(self, id_usuario: int, nombre: str, apellido: str, mail: str):
        usuario = self.repo.obtener_por_id(id_usuario)
        if not usuario:
            return False
 
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.mail = mail
        self.repo.actualizar(usuario)
        return True
    
    # UPDATE - Contraseña, validando la actual
    def cambiar_contrasena(self, id_usuario: int, contrasena_actual: str, contrasena_nueva: str):
        usuario = self.repo.obtener_por_id(id_usuario)
        if not usuario:
            return None, "Usuario no encontrado"
        if not usuario.validar_contraseña(contrasena_actual): # Método de validación ya existe en la clase Usuario
            return None, "Contraseña actual incorrecta"
 
        usuario.contraseña = contrasena_nueva
        self.repo.actualizar(usuario)
        return True, None

    # DELETE
    def eliminar(self, id_usuario: int):
        usuario = self.repo.obtener_por_id(id_usuario)
        if not usuario:
            return False
        self.repo.eliminar(id_usuario)
        return True
 
    # Serialización
    def _serializar(self, usuario) -> dict:
        return {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "mail": usuario.mail,
            "activo": usuario.activo,
            "fecha_creacion": str(usuario.fechaCreacion),
            "fecha_modificacion": str(usuario.fechaModificacion),
        }