from Repositories import TableroRepository, UsuarioRepository
from Classes import Tablero
from datetime import datetime

class TableroService:
    def __init__(self):
        self.repo = TableroRepository()

    # READ
    def obtener_por_id(self, id_tablero: int):
        tablero = self.repo.obtener_por_id(id_tablero)
        if not tablero:
            return None
        return self._serializar(tablero)
    def obtener_todos(self, id_usuario):
        tableros = self.repo.obtener_todos(id_usuario) 
        return [self._serializar(t) for t in tableros]   
    
    # CREATE
    def crear(self, nombre: str, descripcion: str, id_propietario: int):
        repo_usuario = UsuarioRepository()
        propietario = repo_usuario.obtener_por_id(id_propietario)
        if not propietario: # Catch de posible error
            return False
        
        nuevo = Tablero(
            id=None,
            fechaCreacion=datetime.now(),
            fechaModificacion=datetime.now(),
            nombre=nombre,
            descripcion=descripcion,
            estados=[],
            propietario=propietario
        )
        self.repo.crear(nuevo)
        return True

    # UPDATE
    def actualizar_datos(self, id_tablero: int, nombre: str, descripcion: str):
        tablero = self.repo.obtener_por_id(id_tablero)
        if not tablero:
            return False
        
        tablero.nombre = nombre
        tablero.descripcion = descripcion
        self.repo.actualizar(tablero)
        return True
    
    # DELETE
    def eliminar(self, id_tablero: int):
        tablero = self.repo.obtener_por_id(id_tablero)
        if not tablero:
            return False
        self.repo.eliminar(id_tablero)
        return True

    # Serialización
    def _serializar(self, tablero):
        return{
            "id": tablero.id,
            "nombre": tablero.nombre,
            "descripcion": tablero.descripcion,
            "propietario_id": tablero.propietario.id,
            "fecha_creacion": str(tablero.fechaCreacion),
            "fecha_modificacion": str(tablero.fechaModificacion),
        }