import { useState, useEffect } from 'react'
import toast from 'react-hot-toast'
import { cargarComentariosDeTarea } from '../../api/comentarios'

const PRIORIDADES = {
  alta:  { label: 'Alta',  color: '#ef4444' },
  media: { label: 'Media', color: '#f59e0b' },
  baja:  { label: 'Baja',  color: '#22c55e' },
}

function formatearFecha(iso) {
  if (!iso) return ''
  try {
    return new Date(iso).toLocaleString('es-AR', {
      day: '2-digit',
      month: 'short',
      hour: '2-digit',
      minute: '2-digit',
    })
  } catch {
    return iso
  }
}

export default function TareaDetalleModal({
  tarea,
  usuarioId,
  onCerrar,
  onAgregarComentario,
  onEditarComentario,
  onEliminarComentario,
  onEditar,
}) {
  const [textoComentario, setTextoComentario] = useState('')
  const [comentarios, setComentarios] = useState(tarea.comentarios ?? [])
  const [cargandoComentarios, setCargandoComentarios] = useState(true)
  const [enviando, setEnviando] = useState(false)
  const [editandoId, setEditandoId] = useState(null)
  const [textoEdicion, setTextoEdicion] = useState('')

  const prio = PRIORIDADES[tarea.prioridad] ?? PRIORIDADES.media

  useEffect(() => {
    let cancelado = false
    setCargandoComentarios(true)

    cargarComentariosDeTarea(tarea.id)
      .then(lista => {
        if (!cancelado) setComentarios(lista)
      })
      .catch(err => {
        if (!cancelado) toast.error(err.message ?? 'No se pudieron cargar los comentarios')
      })
      .finally(() => {
        if (!cancelado) setCargandoComentarios(false)
      })

    return () => { cancelado = true }
  }, [tarea.id])

  useEffect(() => {
    setComentarios(tarea.comentarios ?? [])
  }, [tarea.comentarios])

  const handleEnviarComentario = async () => {
    const contenido = textoComentario.trim()
    if (!contenido || enviando) return

    setEnviando(true)
    try {
      await onAgregarComentario(tarea.id, contenido)
      setTextoComentario('')
    } catch (err) {
      toast.error(err.message ?? 'No se pudo guardar el comentario')
    } finally {
      setEnviando(false)
    }
  }

  const iniciarEdicion = (c) => {
    setEditandoId(c.id)
    setTextoEdicion(c.contenido)
  }

  const cancelarEdicion = () => {
    setEditandoId(null)
    setTextoEdicion('')
  }

  const guardarEdicion = async (idComentario) => {
    const contenido = textoEdicion.trim()
    if (!contenido) return

    setEnviando(true)
    try {
      await onEditarComentario(tarea.id, idComentario, contenido)
      cancelarEdicion()
    } catch (err) {
      toast.error(err.message ?? 'No se pudo actualizar el comentario')
    } finally {
      setEnviando(false)
    }
  }

  const handleEliminar = async (idComentario) => {
    if (!window.confirm('¿Eliminar este comentario?')) return

    setEnviando(true)
    try {
      await onEliminarComentario(tarea.id, idComentario)
      if (editandoId === idComentario) cancelarEdicion()
    } catch (err) {
      toast.error(err.message ?? 'No se pudo eliminar el comentario')
    } finally {
      setEnviando(false)
    }
  }

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleEnviarComentario()
    }
  }

  return (
    <div className="modal-overlay" onClick={onCerrar}>
      <div className="modal-box modal-box--detalle" onClick={e => e.stopPropagation()}>
        <div className="modal-header">
          <div className="detalle-header-meta">
            <span className="tarea-prio-badge" style={{ color: prio.color, borderColor: prio.color }}>
              {prio.label}
            </span>
            <span className="detalle-id">#{tarea.id}</span>
          </div>
          <div className="detalle-header-actions">
            <button type="button" className="btn-secondary btn-sm" onClick={() => onEditar(tarea)}>
              Editar
            </button>
            <button type="button" className="btn-icon modal-close" onClick={onCerrar} aria-label="Cerrar">
              ✕
            </button>
          </div>
        </div>

        <div className="modal-body detalle-body">
          <h2 className="detalle-titulo">{tarea.titulo}</h2>

          <section className="detalle-seccion">
            <h3>Descripción</h3>
            <p className="detalle-descripcion">
              {tarea.descripcion?.trim() ? tarea.descripcion : 'Sin descripción.'}
            </p>
          </section>

          <section className="detalle-seccion detalle-comentarios">
            <h3>Comentarios <span className="detalle-count">({comentarios.length})</span></h3>

            {cargandoComentarios ? (
              <p className="comentarios-vacio">Cargando comentarios...</p>
            ) : (
              <ul className="comentarios-lista">
                {comentarios.length === 0 && (
                  <li className="comentarios-vacio">Todavía no hay comentarios.</li>
                )}
                {comentarios.map(c => {
                  const esPropio = c.usuarioId === usuarioId
                  const enEdicion = editandoId === c.id

                  return (
                    <li key={c.id} className="comentario-item">
                      <div className="comentario-cabecera">
                        <span className="comentario-autor">{c.autor}</span>
                        <div className="comentario-cabecera-derecha">
                          <span className="comentario-fecha">{formatearFecha(c.fechaCreacion)}</span>
                          {esPropio && !enEdicion && (
                            <div className="comentario-acciones">
                              <button type="button" className="btn-icon btn-sm-icon" title="Editar" onClick={() => iniciarEdicion(c)}>✎</button>
                              <button type="button" className="btn-icon btn-sm-icon btn-danger" title="Eliminar" onClick={() => handleEliminar(c.id)}>✕</button>
                            </div>
                          )}
                        </div>
                      </div>
                      {enEdicion ? (
                        <div className="comentario-edicion">
                          <textarea
                            className="modal-input modal-textarea"
                            value={textoEdicion}
                            onChange={e => setTextoEdicion(e.target.value)}
                            rows={2}
                            disabled={enviando}
                          />
                          <div className="comentario-edicion-botones">
                            <button type="button" className="btn-secondary btn-sm" onClick={cancelarEdicion} disabled={enviando}>
                              Cancelar
                            </button>
                            <button
                              type="button"
                              className="btn-primary btn-sm"
                              onClick={() => guardarEdicion(c.id)}
                              disabled={!textoEdicion.trim() || enviando}
                            >
                              Guardar
                            </button>
                          </div>
                        </div>
                      ) : (
                        <p className="comentario-texto">{c.contenido}</p>
                      )}
                    </li>
                  )
                })}
              </ul>
            )}

            <div className="comentario-form">
              <textarea
                className="modal-input modal-textarea comentario-input"
                placeholder="Escribí un comentario..."
                value={textoComentario}
                onChange={e => setTextoComentario(e.target.value)}
                onKeyDown={handleKeyDown}
                rows={3}
                disabled={enviando}
              />
              <button
                type="button"
                className="btn-primary"
                onClick={handleEnviarComentario}
                disabled={!textoComentario.trim() || enviando}
              >
                {enviando ? 'Enviando...' : 'Comentar'}
              </button>
            </div>
          </section>
        </div>
      </div>
    </div>
  )
}
