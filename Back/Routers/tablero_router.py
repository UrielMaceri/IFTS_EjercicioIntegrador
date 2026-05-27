from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from Services.tablero_service import TableroService

router = APIRouter(prefix="/tablero", tags=["Tableros"])
service = TableroService()


""" Modelos Pydantic - DTOs (Data Transfer Objects) """ 
class TableroCrearDTO(BaseModel):
    nombre: str
    descripcion: str
    id_propietario: int

class TableroActualizarDTO(BaseModel):
    nombre: str
    descripcion: str

""" Endpoints """
# GET /tablero/
@router.get("/usuario/{id_usuario}")
def obtener_todos(id_usuario: int):
    return service.obtener_todos(id_usuario)

# GET /tablero/{id}
@router.get("/{id_tablero}")
def obtener_tablero(id_tablero: int):
    tablero = service.obtener_por_id(id_tablero)
    if not tablero:
        raise HTTPException(status_code=404, detail=f"Tablero {id_tablero} no encontrado")
    return tablero

# POST /tablero/
@router.post("/", status_code=201)
def crear_tablero(datos: TableroCrearDTO):
    ok = service.crear(
        nombre=datos.nombre,
        descripcion=datos.descripcion,
        id_propietario=datos.id_propietario
    )
    if not ok:
        raise HTTPException(status_code=404, detail=f"Usuario {datos.id_propietario} no encontrado")
    return {"mensaje":"Tablero creado correctamente"}

# PUT /tablero/{id}
@router.put("/{id_tablero}")
def actualizar_tablero(id_tablero: int, datos: TableroActualizarDTO):
    ok = service.actualizar_datos(
        id_tablero=id_tablero,
        nombre=datos.nombre,
        descripcion=datos.descripcion
    )
    if not ok:
        raise HTTPException(status_code=404, detail=f"Tablero {id_tablero} no encontrado")
    return {"mensaje":"Tablero actualizado correctamente"}

# DETELE /tablero/{id}
@router.delete("/{id_tablero}")
def eliminar_tablero(id_tablero: int):
    ok = service.eliminar(id_tablero)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Tablero {id_tablero} no encontrado")
    return {"mensaje":"Tablero eliminado correctamente"}