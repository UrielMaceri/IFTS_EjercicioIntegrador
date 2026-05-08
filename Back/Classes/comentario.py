from .base import Base

class Comentario(Base):
    def __init__(self, id, fechaCreacion, fechaModificacion, tarea, usuario, contenido, usuarioMod):
        super().__init__(id, fechaCreacion, fechaModificacion)
        self.tarea = tarea
        self.usuario = usuario
        self.contenido = contenido
        self.usuarioMod = usuarioMod

    # Metodos
    # Ver si es necesario agregar un metodo para editar o si se hace desde el repo
    #def editar(self, nuevoContenido, hechoPorUsuario):
    #    self.contenido = nuevoContenido
    #    self.usuarioMod = hechoPorUsuario       

    
    