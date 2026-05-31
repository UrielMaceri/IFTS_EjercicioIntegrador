import { apiFetch } from './config'

export function obtenerEstadosPorTablero(idTablero) {
  return apiFetch(`/estado/tablero/${idTablero}`)
}

export function crearEstado({ nombre, posicion, id_tablero }) {
  return apiFetch('/estado/', {
    method: 'POST',
    body: JSON.stringify({ nombre, posicion, id_tablero }),
  })
}

export function actualizarEstado(idEstado, { nombre, posicion }) {
  return apiFetch(`/estado/${idEstado}`, {
    method: 'PUT',
    body: JSON.stringify({ nombre, posicion }),
  })
}

export function eliminarEstado(idEstado) {
  return apiFetch(`/estado/${idEstado}`, { method: 'DELETE' })
}
