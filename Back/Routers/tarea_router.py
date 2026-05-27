from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from Services import TareaService
from datetime import datetime
 
router = APIRouter(prefix="/tarea", tags=["Tareas"])
service = TareaService()

""" Modelos Pydantic - DTOs (Data Transfer Objects) """ 
class TareaCrearDTO(BaseModel):
    titulo: str
    descripcion: str
    prioridad: int
    id_estado: int
    id_usuario_asignado: int
    fecha_vencimiento: datetime
    posicion: int
 
class TareaActualizarDTO(BaseModel):
    titulo: str
    descripcion: str
    prioridad: int
    fecha_vencimiento: datetime
    posicion: int
 
class TareaMoverDTO(BaseModel):
    id_estado_nuevo: int
 
class TareaAsignarDTO(BaseModel):
    id_usuario: int


""" Endpoints """
# GET /tarea/estado/{id}
@router.get("/estado/{id_estado}")
def obtener_todos(id_estado: int):
    return service.obtener_todos(id_estado)
 
# GET /tarea/{id}
@router.get("/{id_tarea}")
def obtener_tarea(id_tarea: int):
    tarea = service.obtener_por_id(id_tarea)
    if not tarea:
        raise HTTPException(status_code=404, detail=f"Tarea {id_tarea} no encontrada")
    return tarea

# POST /tarea/
@router.post("/", status_code=201)
def crear_tarea(datos: TareaCrearDTO):
    ok, error = service.crear(
        titulo=datos.titulo,
        descripcion=datos.descripcion,
        prioridad=datos.prioridad,
        id_estado=datos.id_estado,
        fecha_vencimiento=datos.fecha_vencimiento,
        id_usuario_asignado=datos.id_usuario_asignado,
        posicion=datos.posicion
    )
    if not ok:
        raise HTTPException(status_code=404, detail=error)
    return {"mensaje": "Tarea creada correctamente"}

# PUT /tarea/{id}
@router.put("/{id_tarea}")
def actualizar_tarea(id_tarea: int, datos: TareaActualizarDTO):
    ok = service.actualizar_datos(
        id_tarea=id_tarea,
        titulo=datos.titulo,
        descripcion=datos.descripcion,
        prioridad=datos.prioridad,
        fecha_vencimiento=datos.fecha_vencimiento,
        posicion=datos.posicion
    )
    if not ok:
        raise HTTPException(status_code=404, detail=f"Tarea {id_tarea} no encontrada")
    return {"mensaje": "Tarea actualizada correctamente"}

# PUT /tarea/{id}/mover — cambia la tarea de estado (columna)
@router.put("/{id_tarea}/mover")
def mover_tarea(id_tarea: int, datos: TareaMoverDTO):
    ok, error = service.mover_estado(
        id_tarea=id_tarea,
        id_estado_nuevo=datos.id_estado_nuevo
    )
    if not ok:
        raise HTTPException(status_code=404, detail=error)
    return {"mensaje": "Tarea movida correctamente"}

# PUT /tarea/{id}/asignar — asigna un usuario a la tarea
@router.put("/{id_tarea}/asignar")
def asignar_usuario(id_tarea: int, datos: TareaAsignarDTO):
    ok, error = service.asignar_usuario(
        id_tarea=id_tarea,
        id_usuario=datos.id_usuario
    )
    if not ok:
        raise HTTPException(status_code=404, detail=error)
    return {"mensaje": "Usuario asignado correctamente"}

# DELETE /tarea/{id}
@router.delete("/{id_tarea}")
def eliminar_tarea(id_tarea: int):
    ok = service.eliminar(id_tarea)
    if not ok:
        raise HTTPException(status_code=404, detail=f"Tarea {id_tarea} no encontrada")
    return {"mensaje": "Tarea eliminada correctamente"}