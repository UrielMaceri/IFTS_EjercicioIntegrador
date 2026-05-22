import { useState } from 'react'

const PRIORIDADES = {
  alta:  { label: 'Alta',  color: '#ef4444' },
  media: { label: 'Media', color: '#f59e0b' },
  baja:  { label: 'Baja',  color: '#22c55e' },
}

export default function TareaModal({ estadoId, tarea, onGuardar, onCerrar }) {
  const esEdicion = !!tarea
  const [titulo, setTitulo] = useState(tarea?.titulo ?? '')
  const [descripcion, setDescripcion] = useState(tarea?.descripcion ?? '')
  const [prioridad, setPrioridad] = useState(tarea?.prioridad ?? 'media')

  const handleGuardar = () => {
    if (!titulo.trim()) return
    onGuardar({ titulo: titulo.trim(), descripcion: descripcion.trim(), prioridad }, estadoId, tarea?.id)
  }

  return (
    <div className="modal-overlay" onClick={onCerrar}>
      <div className="modal-box" onClick={e => e.stopPropagation()}>
        <div className="modal-header">
          <h2>{esEdicion ? 'Editar tarea' : 'Nueva tarea'}</h2>
          <button className="btn-icon modal-close" onClick={onCerrar}>✕</button>
        </div>

        <div className="modal-body">
          <label>Título</label>
          <input
            className="modal-input"
            type="text"
            placeholder="Nombre de la tarea"
            value={titulo}
            onChange={e => setTitulo(e.target.value)}
            autoFocus
          />

          <label>Descripción</label>
          <textarea
            className="modal-input modal-textarea"
            placeholder="Descripción opcional..."
            value={descripcion}
            onChange={e => setDescripcion(e.target.value)}
          />

          <label>Prioridad</label>
          <div className="prio-selector">
            {Object.entries(PRIORIDADES).map(([key, val]) => (
              <button
                key={key}
                className={`prio-btn ${prioridad === key ? 'active' : ''}`}
                style={{ '--pcolor': val.color }}
                onClick={() => setPrioridad(key)}
              >
                {val.label}
              </button>
            ))}
          </div>
        </div>

        <div className="modal-footer">
          <button className="btn-secondary" onClick={onCerrar}>Cancelar</button>
          <button className="btn-primary" onClick={handleGuardar}>
            {esEdicion ? 'Guardar cambios' : 'Crear tarea'}
          </button>
        </div>
      </div>
    </div>
  )
}
