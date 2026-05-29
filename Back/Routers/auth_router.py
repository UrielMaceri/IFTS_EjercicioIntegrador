from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from Services import AuthService
 
router = APIRouter(prefix="/auth", tags=["Auth"])
service = AuthService()

""" Modelos Pydantic - DTOs (Data Transfer Objects) """ 
class AuthLogin(BaseModel):
    mail: str
    contrasena: str

""" Endpoints """
# POST /Auth/
@router.post("/")
def authentication(datos: AuthLogin):
    okLogin = service.authenticate(datos.mail, datos.contrasena)
    
    if okLogin is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if okLogin is False:
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    
    return okLogin