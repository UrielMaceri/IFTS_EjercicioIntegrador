from .base import Base

class Comentario(Base):
    def __init__(self, comentarioId, fechaCreacion, fechaModificacion, tareaId, usuarioId, contenido, usuarioMod):
        super().__init__(comentarioId, fechaCreacion, fechaModificacion)
        self.tareaId = tareaId
        self.usuarioId = usuarioId
        self.contenido = contenido
        self.usuarioMod = usuarioMod

    # Metodos
    # Ver si es necesario agregar un metodo para editar o si se hace desde el repo
    #def editar(self, nuevoContenido, hechoPorUsuario):
    #    self.contenido = nuevoContenido
    #    self.usuarioMod = hechoPorUsuario       

    
    