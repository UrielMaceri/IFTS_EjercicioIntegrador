from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routers.usuario_router import router as usuario_router
from Routers.tablero_router import router as tablero_router
from Routers.estado_router import router as estado_router
from Routers.tarea_router import router as tarea_router
from Routers.comentario_router import router as comentario_router
from Routers.auth_router import router as auth_router
 
app = FastAPI()
 
# CORS para cuando haya produccion y el frontend esté en otro dominio. Por ahora, permite todo para facilitar el desarrollo.
# Permite que React (corriendo en otro puerto) pueda hacer fetch al backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
# Para inicializar servicio desde cmd
# uvicorn main:app --reload

# Routers 
app.include_router(usuario_router)
app.include_router(tablero_router)
app.include_router(estado_router)
app.include_router(tarea_router)
app.include_router(comentario_router)
app.include_router(auth_router)
 
# Health check 
@app.get("/")
def raiz():
    return {"status": "ok"}
 