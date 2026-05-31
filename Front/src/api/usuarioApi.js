import { apiFetch } from './config'

const cacheNombres = new Map()

export function limpiarCacheUsuarios() {
  cacheNombres.clear()
}

export function obtenerUsuario(idUsuario) {
  return apiFetch(`/usuario/${idUsuario}`)
}

export async function nombreDeUsuario(idUsuario) {
  if (cacheNombres.has(idUsuario)) return cacheNombres.get(idUsuario)

  try {
    const u = await obtenerUsuario(idUsuario)
    const nombre = [u.nombre, u.apellido].filter(Boolean).join(' ') || u.mail || `Usuario #${idUsuario}`
    cacheNombres.set(idUsuario, nombre)
    return nombre
  } catch {
    return `Usuario #${idUsuario}`
  }
}
