from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from Services.usuario_service import UsuarioService
 
router = APIRouter(prefix="/usuario", tags=["Usuarios"])
service = UsuarioService()
 
 
""" Modelos Pydantic - DTOs (Data Transfer Objects) """ 
class UsuarioCrearDTO(BaseModel):
    nombre: str
    apellido: str
    mail: str
    contrasena: str
 
class UsuarioActualizarDTO(BaseModel):
    nombre: str
    apellido: str
    mail: str
 
class CambiarContrasenaDTO(BaseModel):
    contrasena_actual: str
    contrasena_nueva: str


""" Endpoints """
# GET /usuario/
@router.get("/")
def obtener_todos():
    return service.obtener_todos()

# GET /usuario/{id}
@router.get("/{id_usuario}")
def obtener_usuario(id_usuario: int):
    usuario = service.obtener_por_id(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail=f"Usuario {id_usuario} no encontrado")
    return usuario

# POST /usuario/
@router.post("/", status_code=201)
def crear_usuario(datos: UsuarioCrearDTO):
    service.crear(
        nombre=datos.nombre,
        apellido=datos.apellido,
        mail=datos.mail,
        contrasena=datos.contrasena
    )
    return {"mensaje": "Usuario creado correctamente"}

# PUT /usuario/{id} - SOLO nombre, apellido y mail.
@router.put("/{id_usuario}")
def actualizar_usuario(id_usuario: int, datos: UsuarioActualizarDTO):
    ok = service.actualizar_datos(
        id_usuario=id_usuario,
        nombre=datos.nombre,
        apellido=datos.apellido,
        mail=datos.mail
    )
    if not ok:
        raise HTTPException(status_code=404, detail=f"Usuario {id_usuario} no encontrado")
    return {"mensaje": "Usuario actualizado correctamente"}

# PUT /usuario/{id}/contrasena - Separado del PUT general porque primero valida la actual.
@router.put("/{id_usuario}/contrasena")
def cambiar_contrasena(id_usuario: int, datos: CambiarContrasenaDTO):
    ok, error = service.cambiar_contrasena(
        id_usuario=id_usuario,
        contrasena_actual=datos.contrasena_actual,
        contrasena_nueva=datos.contrasena_nueva
    )
    if error:
        # 404 si no existe el usuario, 400 si la contraseña actual es incorrecta
        if "no encontrado" in error:
            codigo = 404
        else:
            codigo = 400
        raise HTTPException(status_code=codigo, detail=error)
    return {"mensaje": "Contraseña actualizada correctamente"}

# DELETE /usuario/{id}
@router.delete("/{id_usuario}")
def eliminar_usuario(id_usuario: int):
    ok = service.eliminar(id_usuario)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Usuario {id_usuario} no encontrado")
    return {"mensaje": "Usuario eliminado correctamente"}