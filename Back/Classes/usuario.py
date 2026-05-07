from .base import Base

class Usuario(Base):
    def __init__(self, id, fechaCreacion, fechaModificacion, nombre, apellido, mail, contraseña, tableros, activo):
        super().__init__(id, fechaCreacion, fechaModificacion)
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.contraseña = contraseña
        self.tableros = tableros
        self.activo = activo

    # Metodos 
    def activar_desactivar(self):
        if self.activo:
            self.activo = False
        else:
            self.activo = True
    
    def validar_contraseña(self, contraseña):
        return self.contraseña == contraseña
        
    
