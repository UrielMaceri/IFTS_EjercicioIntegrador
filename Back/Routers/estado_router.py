from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from Services import EstadoService

router = APIRouter(prefix="/estado", tags=["Estados"])
service = EstadoService()

""" Modelos Pydantic - DTOs (Data Transfer Objects) """
class EstadoCrearDTO(BaseModel):
    nombre: str
    posicion: int
    id_tablero: int

class EstadoActualizarDTO(BaseModel):
    nombre: str
    posicion: int

""" Endpoints """
# GET /estado/tablero/{id}
@router.get("/tablero/{id_tablero}")
def obtener_todos(id_tablero: int):
    return service.obtener_todos(id_tablero)

# GET /estado/{id}
@router.get("/{id_estado}")
def obtener_estado(id_estado: int):
    estado = service.obtener_por_id(id_estado)
    if not estado:
        raise HTTPException(status_code=404, detail=f"Estado {id_estado} no encontrado")
    return estado

# POST /estado/
@router.post("/", status_code=201)
def crear_estado(datos: EstadoCrearDTO):
    ok = service.crear(
        nombre=datos.nombre,
        posicion=datos.posicion,
        id_tablero=datos.id_tablero
    )
    if not ok:
        raise HTTPException(status_code=404, detail=f"Tablero {datos.id_tablero} no encontrado")
    return {"mensaje":"Estado creado correctamente"}

# PUT /estado/{id}
@router.put("/{id_estado}")
def actualizar_estado(id_estado: int, datos: EstadoActualizarDTO):
    ok = service.actualizar_datos(
        id_estado=id_estado,
        nombre=datos.nombre,
        posicion=datos.posicion,
    )
    if not ok:
        raise HTTPException(status_code=404, detail=f"Estado {id_estado} no encontrado")
    return {"mensaje":"Estado creado correctamente"}

# DETELE /estado/{id}
@router.delete("/{id_estado}")
def eliminar_estado(id_estado: int):
    ok = service.eliminar(id_estado)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Estado {id_estado} no encontrado")
    return {"mensaje":"Estado eliminado correctamente"}