import { apiFetch } from './config'

export function obtenerTareasPorEstado(idEstado) {
  return apiFetch(`/tarea/estado/${idEstado}`)
}

export function crearTarea(body) {
  return apiFetch('/tarea/', {
    method: 'POST',
    body: JSON.stringify(body),
  })
}

export function actualizarTarea(idTarea, body) {
  return apiFetch(`/tarea/${idTarea}`, {
    method: 'PUT',
    body: JSON.stringify(body),
  })
}

export function moverTarea(idTarea, id_estado_nuevo) {
  return apiFetch(`/tarea/${idTarea}/mover`, {
    method: 'PUT',
    body: JSON.stringify({ id_estado_nuevo }),
  })
}

export function eliminarTarea(idTarea) {
  return apiFetch(`/tarea/${idTarea}`, { method: 'DELETE' })
}
