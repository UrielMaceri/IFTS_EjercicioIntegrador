import { useState } from 'react'
import '../styles/KanbanBoard.css'

const COLORES = ['#aa3bff', '#3b82f6', '#f59e0b', '#22c55e', '#ef4444', '#ec4899', '#14b8a6']

export default function EstadoModal({ onGuardar, onCerrar }) {
  const [nombre, setNombre] = useState('')
  const [color, setColor] = useState(COLORES[0])

  return (
    <div className="modal-overlay" onClick={onCerrar}>
      <div className="modal-box modal-box--sm" onClick={e => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Nueva columna</h2>
          <button className="btn-icon modal-close" onClick={onCerrar}>✕</button>
        </div>

        <div className="modal-body">
          <label>Nombre del estado</label>
          <input
            className="modal-input"
            type="text"
            placeholder="Ej: En testing"
            value={nombre}
            onChange={e => setNombre(e.target.value)}
            autoFocus
          />

          <label>Color</label>
          <div className="color-picker">
            {COLORES.map(c => (
              <button
                key={c}
                className={`color-dot ${color === c ? 'selected' : ''}`}
                style={{ background: c }}
                onClick={() => setColor(c)}
              />
            ))}
          </div>
        </div>

        <div className="modal-footer">
          <button className="btn-secondary" onClick={onCerrar}>Cancelar</button>
          <button
            className="btn-primary"
            onClick={() => { if (nombre.trim()) onGuardar(nombre.trim(), color) }}
          >
            Crear columna
          </button>
        </div>
      </div>
    </div>
  )
}
