import { obtenerTablero } from './tableroApi'
import { obtenerEstadosPorTablero } from './estadoApi'
import { obtenerTareasPorEstado } from './tareaApi'
import { cargarComentariosDeTarea } from './comentarios'
import { prioridadFromApi } from './prioridad'

const COLORES_ESTADO = ['#aa3bff', '#3b82f6', '#22c55e', '#f59e0b', '#ef4444', '#ec4899']

async function mapTareaConComentarios(t) {
  let comentarios = []
  try {
    comentarios = await cargarComentariosDeTarea(t.id)
  } catch {
    comentarios = []
  }
  return {
    id: t.id,
    titulo: t.titulo,
    descripcion: t.descripcion ?? '',
    prioridad: prioridadFromApi(t.prioridad),
    comentarios,
    fechaVencimiento: t.fecha_vencimiento,
    posicion: t.posicion,
  }
}

export async function cargarTableroCompleto(idTablero) {
  const tablero = await obtenerTablero(idTablero)
  const estadosApi = await obtenerEstadosPorTablero(idTablero)
  const ordenados = [...estadosApi].sort((a, b) => a.posicion - b.posicion)

  const estados = await Promise.all(
    ordenados.map(async (e, i) => {
      const tareasApi = await obtenerTareasPorEstado(e.id)
      const tareas = await Promise.all(tareasApi.map(mapTareaConComentarios))
      return {
        id: e.id,
        nombre: e.nombre,
        posicion: e.posicion,
        tareas,
      }
    })
  )

  return { tablero, estados }
}
