from .base import Base

class Tarea(Base):
    def __init__(self, id, fechaCreacion, fechaModificacion, titulo, descripcion, prioridad, usuarioAsignado, fechaVencimiento, posicion):
        super().__init__(id, fechaCreacion, fechaModificacion)
        self.titulo = titulo
        self.descripcion = descripcion 
        self.prioridad = prioridad
        self.usuarioAsignado = usuarioAsignado
        self.fechaVencimiento = fechaVencimiento
        self.posicion = posicion

    # Metodos
    
    def cambiar_prioridad(self, nuevaPrioridad):
        self.prioridad = nuevaPrioridad

    def asignar_usuario(self, nuevoAsignado):
        self.usuarioAsignado = nuevoAsignado

    def cambiar_estado(self, nuevoEstado):
        self.estado = nuevoEstado

    def editar(self, nuevoTitulo, nuevaDescripcion):
        if nuevoTitulo:
            self.titulo = nuevoTitulo
        if nuevaDescripcion:
            self.descripcion = nuevaDescripcion

    

