import { apiFetch } from './config'

export function obtenerTablerosPorUsuario(idUsuario) {
  return apiFetch(`/tablero/usuario/${idUsuario}/`)
}

export function obtenerTablero(idTablero) {
  return apiFetch(`/tablero/${idTablero}/`)
}

export function crearTablero({ nombre, descripcion, id_propietario }) {
  return apiFetch('/tablero/', {
    method: 'POST',
    body: JSON.stringify({ nombre, descripcion, id_propietario }),
  })
}

export function eliminarTablero(idTablero) {
  return apiFetch(`/tablero/${idTablero}`, { method: 'DELETE' })
}
