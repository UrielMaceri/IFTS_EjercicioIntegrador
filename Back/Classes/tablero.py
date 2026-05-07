from .base import Base

class Tablero(Base):
    def __init__(self, id, fechaCreacion, fechaModificacion, nombre, descripcion, estados, propietario):
        super().__init__(id, fechaCreacion, fechaModificacion)
        self.nombre = nombre
        self.descripcion = descripcion
        self.estados = estados
        self.propietario = propietario

    # Metodos
    def agregar_estado(self, nuevoEstado):
        self.estados.append(nuevoEstado)

    def eliminar_estado(self, estadoId):
        for estado in self.estados:
            if estado.id == estadoId:
                self.estados.remove(estado)
                break        

        
    

