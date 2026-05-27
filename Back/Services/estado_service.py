from Repositories import EstadoRepository, TableroRepository
from Classes import Estado
from datetime import datetime

class EstadoService:
    def __init__(self):
        self.repo = EstadoRepository()

    # READ
    def obtener_por_id(self, id_estado: int):
        estado = self.repo.obtener_por_id(id_estado)
        if not estado:
            return None
        return self._serializar(estado)
    def obtener_todos(self, id_tablero):
        estados = self.repo.obtener_todos(id_tablero)
        return [self._serializar(e) for e in estados]
    
    # CREATE
    def crear(self, nombre: str, posicion: int, id_tablero: int):
        repo_tablero = TableroRepository()
        tableroPadre = repo_tablero.obtener_por_id(id_tablero)
        if not tableroPadre: 
            return False
        
        nuevo = Estado(
            id=None,
            fechaCreacion=datetime.now(),
            fechaModificacion=datetime.now(),
            nombre=nombre,
            posicion=posicion,
            tablero=tableroPadre,
            tareas=[]
        )
        self.repo.crear(nuevo)
        return True
    
    # UPDATE
    def actualizar_datos(self, id_estado: int, nombre: str, posicion: int):
        estado = self.repo.obtener_por_id(id_estado)
        if not estado:
            return False
        
        estado.nombre = nombre
        estado.posicion = posicion
        self.repo.actualizar(estado)
        return True
    
    # DELETE
    def eliminar(self, id_estado: int):
        estado = self.repo.obtener_por_id(id_estado)
        if not estado:
            return False
        self.repo.eliminar(id_estado)
        return True
    
    # Serialización
    def _serializar(self, estado) -> dict:
        return{
            "id": estado.id,
            "nombre": estado.nombre,
            "posicion": estado.posicion,
            "tablero_id": estado.tablero.id,
            "fecha_creacion": str(estado.fechaCreacion),
            "fecha_modificacion": str(estado.fechaModificacion),
        }