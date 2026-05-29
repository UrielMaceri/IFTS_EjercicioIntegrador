from .base import Base

class Usuario(Base):
    def __init__(self, id, fechaCreacion, fechaModificacion, nombre, apellido, mail, contrasena, tableros, activo):
        super().__init__(id, fechaCreacion, fechaModificacion)
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.contrasena = contrasena
        self.tableros = tableros
        self.activo = activo

    # Metodos 
    def activar_desactivar(self):
        if self.activo:
            self.activo = False
        else:
            self.activo = True
    
    def validar_contrasena(self, contrasena):
        return self.contrasena == contrasena
        
    
