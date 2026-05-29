from Repositories import UsuarioRepository
from Classes import Usuario
 
class AuthService:
    def __init__(self):
        self.repo = UsuarioRepository()
    
    # Auth
    def authenticate(self, mail: str, contrasena: str):
        usuario = self.repo.obtener_por_mail(mail)
        if not usuario:
            return None
        
        okLogin = usuario.validar_contrasena(contrasena)
        if not okLogin:
            return False

        return self._serializar(usuario)
    
    def _serializar(self, usuario) -> dict:
        return {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "mail": usuario.mail
        }