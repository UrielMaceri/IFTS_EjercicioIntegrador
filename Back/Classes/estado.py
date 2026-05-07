from .base import Base

class Estado(Base):
    def __init__(self, id, fechaCreacion, fechaModificacion, nombre, posicion, tareas):
        super().__init__(id, fechaCreacion, fechaModificacion)
        self.nombre = nombre
        self.posicion = posicion
        self.tareas = tareas

    
    # Metodos
    def agregar_tarea(self, nuevaTarea):
        self.tareas.append(nuevaTarea)

    def eliminar_tarea(self, tareaId):
        for t in self.tareas:
            if t == tareaId:
                self.tareas.remove(t)
                break
