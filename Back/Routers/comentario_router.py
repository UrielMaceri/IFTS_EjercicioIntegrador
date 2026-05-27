from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from Services import ComentarioService
 
router = APIRouter(prefix="/comentario", tags=["Comentarios"])
service = ComentarioService()
 
 
""" Modelos Pydantic - DTOs (Data Transfer Objects) """ 
class ComentarioCrearDTO(BaseModel):
    id_tarea: int
    id_usuario: int
    contenido: str
 
class ComentarioActualizarDTO(BaseModel):
    contenido: str
    id_usuario_mod: int


""" Endpoints """
# GET /comentario/tarea/{id_tarea}
@router.get("/tarea/{id_tarea}")
def obtener_todos(id_tarea: int):
    return service.obtener_todos(id_tarea)

# GET /comentario/{id}
@router.get("/{id_comentario}")
def obtener_comentario(id_comentario: int):
    comentario = service.obtener_por_id(id_comentario)
    if not comentario:
        raise HTTPException(status_code=404, detail=f"Comentario {id_comentario} no encontrado")
    return comentario

# POST /comentario/
@router.post("/", status_code=201)
def crear_comentario(datos: ComentarioCrearDTO):
    ok, error = service.crear(
        id_tarea=datos.id_tarea,
        id_usuario=datos.id_usuario,
        contenido=datos.contenido
    )
    if not ok:
        raise HTTPException(status_code=404, detail=error)
    return {"mensaje": "Comentario creado correctamente"}

# PUT /comentario/{id}
@router.put("/{id_comentario}")
def actualizar_comentario(id_comentario: int, datos: ComentarioActualizarDTO):
    ok, error = service.actualizar_contenido(
        id_comentario=id_comentario,
        contenido=datos.contenido,
        id_usuario_mod=datos.id_usuario_mod
    )
    if not ok:
        raise HTTPException(status_code=404, detail=error)
    return {"mensaje": "Comentario actualizado correctamente"}

# DELETE /comentario/{id}
@router.delete("/{id_comentario}")
def eliminar_comentario(id_comentario: int):
    ok = service.eliminar(id_comentario)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Comentario {id_comentario} no encontrado")
    return {"mensaje": "Comentario eliminado correctamente"}