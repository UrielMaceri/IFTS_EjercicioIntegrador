import { obtenerComentariosPorTarea } from './comentarioApi'
import { nombreDeUsuario } from './usuarioApi'

export async function cargarComentariosDeTarea(idTarea) {
  const lista = await obtenerComentariosPorTarea(idTarea)
  const ordenados = [...lista].sort(
    (a, b) => new Date(a.fecha_creacion) - new Date(b.fecha_creacion)
  )

  return Promise.all(
    ordenados.map(async c => ({
      id: c.id,
      contenido: c.contenido,
      autor: await nombreDeUsuario(c.usuario_id),
      fechaCreacion: c.fecha_creacion,
      usuarioId: c.usuario_id,
    }))
  )
}
