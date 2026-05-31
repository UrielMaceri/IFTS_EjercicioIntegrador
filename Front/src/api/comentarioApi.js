import { apiFetch } from './config'

export function obtenerComentariosPorTarea(idTarea) {
  return apiFetch(`/comentario/tarea/${idTarea}`)
}

export function crearComentario({ id_tarea, id_usuario, contenido }) {
  return apiFetch('/comentario/', {
    method: 'POST',
    body: JSON.stringify({ id_tarea, id_usuario, contenido }),
  })
}

export function actualizarComentario(idComentario, { contenido, id_usuario_mod }) {
  return apiFetch(`/comentario/${idComentario}`, {
    method: 'PUT',
    body: JSON.stringify({ contenido, id_usuario_mod }),
  })
}

export function eliminarComentario(idComentario) {
  return apiFetch(`/comentario/${idComentario}`, { method: 'DELETE' })
}
