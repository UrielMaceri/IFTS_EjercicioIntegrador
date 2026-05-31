import { useState } from 'react'

const PRIORIDADES = {
  alta:  { label: 'Alta',  color: '#ef4444' },
  media: { label: 'Media', color: '#f59e0b' },
  baja:  { label: 'Baja',  color: '#22c55e' },
}

export default function TareaCard({ tarea, estadoId, onMover, onEliminar, onEditar, onVerDetalle, estados }) {
  const [menuOpen, setMenuOpen] = useState(false)
  const prio = PRIORIDADES[tarea.prioridad] ?? PRIORIDADES.media

  return (
    <div className="tarea-card" draggable>
      <span className="tarea-prio" style={{ background: prio.color }} title={`Prioridad: ${prio.label}`} />

      <button
        type="button"
        className="tarea-body tarea-body-clickable"
        onClick={() => onVerDetalle(tarea, estadoId)}
      >
        <p className="tarea-titulo">{tarea.titulo}</p>
      </button>

      <div className="tarea-footer" onClick={e => e.stopPropagation()}>
        <span className="tarea-prio-badge" style={{ color: prio.color, borderColor: prio.color }}>
          {prio.label}
        </span>

        <div className="tarea-actions">
          <div className="move-menu-wrapper">
            <button type="button" className="btn-icon" title="Mover" onClick={e => { e.stopPropagation(); setMenuOpen(o => !o) }}>
              ⇄
            </button>
            {menuOpen && (
              <div className="move-menu">
                {estados
                  .filter(e => e.id !== estadoId)
                  .map(e => (
                    <button key={e.id} type="button" onClick={() => { onMover(tarea.id, estadoId, e.id); setMenuOpen(false) }}>
                      <span className="move-dot" style={{ background: e.color }} />
                      {e.nombre}
                    </button>
                  ))}
              </div>
            )}
          </div>

          <button type="button" className="btn-icon" title="Editar" onClick={e => { e.stopPropagation(); onEditar(tarea, estadoId) }}>✎</button>
          <button type="button" className="btn-icon btn-danger" title="Eliminar" onClick={e => { e.stopPropagation(); onEliminar(tarea.id, estadoId) }}>✕</button>
        </div>
      </div>
    </div>
  )
}
