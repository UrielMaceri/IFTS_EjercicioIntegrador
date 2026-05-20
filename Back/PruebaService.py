from datetime import datetime

# =========================================================
# CLASSES
# =========================================================

from Classes import Estado, Tablero, Usuario, Tarea, Comentario

# =========================================================
# SERVICES
# =========================================================

from Services import EstadoService, TableroService, UsuarioService, TareaService

# =========================================================
# REPOSITORIES
# =========================================================

from Repositories import UsuarioRepository, TableroRepository, EstadoRepository, TareaRepository, ComentarioRepository

usuario_repo = UsuarioRepository()
tablero_repo = TableroRepository()
estado_repo = EstadoRepository()
tarea_repo = TareaRepository()
comentario_repo = ComentarioRepository()


# =========================================================
# CLASES DE PRUEBA 
# =========================================================

Tarea1 = Tarea(1, datetime.today(), datetime.today(), "Tarea 1", "Descripcion de Tarea 1",1 ,"Usuario1", "2024-12-31",1)
Tarea2 = Tarea(2, datetime.today(), datetime.today(), "Tarea 2", "Descripcion de Tarea 2",1 ,"Usuario1", "2024-12-31",1)
Tarea3 = Tarea(3, datetime.today(), datetime.today(), "Tarea 3", "Descripcion de Tarea 3",1 ,"Usuario1", "2024-12-31",1)
Estado1 = Estado(1, datetime.today(), datetime.today(), "Estado 1", 1, [])
Estado2 = Estado(2, datetime.today(), datetime.today(), "Estado 2", 2, [])
Estado3 = Estado(3, datetime.today(), datetime.today(), "Estado 3", 3, [])
Estado4 = Estado(4, datetime.today(), datetime.today(), "Estado 4", 4, [])
Estado5 = Estado(5, datetime.today(), datetime.today(), "Estado 5", 5, [])
Tablero1 = Tablero(1, datetime.today(), datetime.today(), "Tablero de Prueba", "Descripcion de prueba", [], "Usuario1")

# (Comentadas las asignaciones por BBDD para subir al repositorio y probar sin necesidad de levantar la base de datos)
# Tarea1 = tarea_repo.obtener_por_id(1)
# Tarea2 = tarea_repo.obtener_por_id(2)
# Tarea3 = tarea_repo.obtener_por_id(3)
# Estado1 = estado_repo.obtener_por_id(1)
# Estado2 = estado_repo.obtener_por_id(2)
# Estado3 = estado_repo.obtener_por_id(3)
# Estado4 = estado_repo.obtener_por_id(4)
# Estado5 = estado_repo.obtener_por_id(5)
# Tablero1 = tablero_repo.obtener_por_id(1)

# Cargo las colecciones por separado para probar el metodo #
Estado1.agregar_tarea(Tarea1)
Estado2.agregar_tarea(Tarea2)
Estado3.agregar_tarea(Tarea3)
Tablero1.agregar_estado(Estado1)
Tablero1.agregar_estado(Estado2)
Tablero1.agregar_estado(Estado3)
Tablero1.agregar_estado(Estado4)
Tablero1.agregar_estado(Estado5)

# =========================================================
# PRUEBA REORDENAR ESTADOS
# =========================================================

for estado in Tablero1.estados:
    print(estado.nombre)

print("-------------------------------")

TableroS = TableroService()
TableroS.reordenar_estado(Tablero1, 4, 0)

for estado in Tablero1.estados:
    print(estado.nombre)

