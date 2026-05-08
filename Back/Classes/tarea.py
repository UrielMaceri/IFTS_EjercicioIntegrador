from .base import Base

class Tarea(Base):
    def __init__(self, id, fechaCreacion, fechaModificacion, titulo, descripcion, prioridad, estado, usuarioAsignado, fechaVencimiento, posicion, comentarios):
        super().__init__(id, fechaCreacion, fechaModificacion)
        self.titulo = titulo
        self.descripcion = descripcion 
        self.prioridad = prioridad
        self.estado = estado
        self.usuarioAsignado = usuarioAsignado
        self.fechaVencimiento = fechaVencimiento
        self.posicion = posicion
        self.comentarios = comentarios

    # Metodos
    def cambiar_prioridad(self, nuevaPrioridad):
        self.prioridad = nuevaPrioridad

    def asignar_usuario(self, nuevoAsignado):
        self.usuarioAsignado = nuevoAsignado

    def cambiar_estado(self, nuevoEstado):
        self.estado = nuevoEstado

    def agregar_comentario(self, nuevoComentario):
        self.comentarios.append(nuevoComentario)

    def eliminar_comentario(self, comentarioId):
        for c in self.comentarios:
            if c.id == comentarioId:
                self.comentarios.remove(c)
                break


    # Ver si es necesario agregar un metodo para editar o si se hace desde el repo
    #def editar(self, nuevoTitulo, nuevaDescripcion):
    #    if nuevoTitulo:
    #        self.titulo = nuevoTitulo
    #    if nuevaDescripcion:
    #        self.descripcion = nuevaDescripcion

    

