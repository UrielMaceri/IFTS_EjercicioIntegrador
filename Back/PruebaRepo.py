from datetime import datetime, timedelta

# =========================================================
# CLASSES
# =========================================================

from Classes import Usuario, Tablero, Estado, Tarea, Comentario

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
# CREAR USUARIO
# =========================================================

usuario = Usuario(
    None,
    datetime.now(),
    datetime.now(),
    "Uri",
    "Dev",
    "uri@mail.com",
    "1234",
    [],
    True
)

usuario_repo.crear(usuario)
print("Usuario creado")


# =========================================================
# OBTENER USUARIO
# =========================================================

# usuario = usuario_repo.obtener_por_id(1)
#
# print(usuario.id)
# print(usuario.nombre)
# print(usuario.mail)
# print(usuario.activo)


# =========================================================
# ACTUALIZAR USUARIO
# =========================================================

# usuario = usuario_repo.obtener_por_id(1)
#
# usuario.nombre = "Uriel"
# usuario.apellido = "Developer"
# usuario_repo.actualizar(usuario)
#
# print("Usuario actualizado")


# =========================================================
# CREAR TABLERO
# =========================================================

# propietario = usuario_repo.obtener_por_id(1)

# tablero = Tablero(
#     None,
#     datetime.now(),
#     datetime.now(),
#     "Proyecto POO",
#     "Tablero principal",
#     [],
#     propietario
# )

# tablero_repo.crear(tablero)
# print("Tablero creado")


# =========================================================
# OBTENER TABLERO
# =========================================================

# tablero = tablero_repo.obtener_por_id(1)
#
# print(tablero.id)
# print(tablero.nombre)
# print(tablero.descripcion)
# print(tablero.propietario.nombre)


# =========================================================
# ACTUALIZAR TABLERO
# =========================================================

# tablero = tablero_repo.obtener_por_id(1)
#
# tablero.nombre = "Proyecto Backend"
# tablero.descripcion = "Descripcion nueva"
#
# tablero_repo.actualizar(tablero)
# print("Tablero actualizado")


# =========================================================
# CREAR ESTADO
# =========================================================

# tablero = tablero_repo.obtener_por_id(1)

# estado = Estado(
#     None,
#     datetime.now(),
#     datetime.now(),
#     "Pendiente",
#     1,
#     tablero,
#     []
# )

# estado_repo.crear(estado)
# print("Estado creado")


# =========================================================
# OBTENER ESTADO
# =========================================================

# estado = estado_repo.obtener_por_id(1)
#
# print(estado.id)
# print(estado.nombre)
# print(estado.posicion)
# print(estado.tablero.nombre)


# =========================================================
# ACTUALIZAR ESTADO
# =========================================================

# estado = estado_repo.obtener_por_id(1)
#
# estado.nombre = "En progreso"
# estado.posicion = 2
#
# estado_repo.actualizar(estado)
# print("Estado actualizado")


# =========================================================
# CREAR TAREA
# =========================================================

# usuario = usuario_repo.obtener_por_id(1)
# estado = estado_repo.obtener_por_id(1)

# tarea = Tarea(
#     None,
#     datetime.now(),
#     datetime.now(),
#     "Terminar TP",
#     "Hacer repositories",
#     1,
#     estado,
#     usuario,
#     datetime.now() + timedelta(days=7),
#     1,
#     []
# )

# tarea_repo.crear(tarea)
# print("Tarea creada")


# =========================================================
# OBTENER TAREA
# =========================================================

# tarea = tarea_repo.obtener_por_id(1)
#
# print(tarea.id)
# print(tarea.titulo)
# print(tarea.descripcion)
# print(tarea.estado.nombre)
# print(tarea.usuarioAsignado.nombre)


# =========================================================
# ACTUALIZAR TAREA
# =========================================================

# tarea = tarea_repo.obtener_por_id(1)
#
# tarea.titulo = "TP COMPLETO"
# tarea.descripcion = "Ahora sí"
# tarea.prioridad = 3
#
# tarea_repo.actualizar(tarea)
# print("Tarea actualizada")


# =========================================================
# CREAR COMENTARIO
# =========================================================

# usuario = usuario_repo.obtener_por_id(1)
# tarea = tarea_repo.obtener_por_id(1)

# comentario = Comentario(
#     None,
#     datetime.now(),
#     datetime.now(),
#     tarea,
#     usuario,
#     "Probando comentarios",
#     usuario
# )

# comentario_repo.crear(comentario)
# print("Comentario creado")


# =========================================================
# OBTENER COMENTARIO
# =========================================================

# comentario = comentario_repo.obtener_por_id(1)
#
# print(comentario.id)
# print(comentario.contenido)
# print(comentario.usuario.nombre)
# print(comentario.tarea.titulo)


# =========================================================
# ACTUALIZAR COMENTARIO
# =========================================================

# comentario = comentario_repo.obtener_por_id(1)
#
# comentario.contenido = "Comentario editado"
# comentario_repo.actualizar(comentario)
#
# print("Comentario actualizado")


# =========================================================
# OBTENER TODOS
# =========================================================

# usuarios = usuario_repo.obtener_todos()
# for u in usuarios:
#     print(u.nombre)

# tableros = tablero_repo.obtener_todos()
# for t in tableros:
#     print(t.nombre)

# estados = estado_repo.obtener_todos()
# for e in estados:
#     print(e.nombre)

# tareas = tarea_repo.obtener_todos()
# for t in tareas:
#     print(t.titulo)

# comentarios = comentario_repo.obtener_todos()
# for c in comentarios:
#     print(c.contenido)


# =========================================================
# DELETE COMENTARIO
# =========================================================

# comentario_repo.eliminar(1)
# print("Comentario eliminado")


# =========================================================
# DELETE TAREA
# =========================================================

# tarea_repo.eliminar(1)
# print("Tarea eliminada")


# =========================================================
# DELETE ESTADO
# =========================================================

# estado_repo.eliminar(1)
# print("Estado eliminado")


# =========================================================
# DELETE TABLERO
# =========================================================

# tablero_repo.eliminar(1)
# print("Tablero eliminado")


# =========================================================
# DELETE USUARIO
# =========================================================

# usuario_repo.eliminar(1)
# print("Usuario eliminado")
