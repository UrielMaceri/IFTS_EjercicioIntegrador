import { useState } from 'react'
import '../styles/KanbanBoard.css'

export default function EstadoModal({ onGuardar, onCerrar }) {
  const [nombre, setNombre] = useState('')

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

        </div>

        <div className="modal-footer">
          <button className="btn-secondary" onClick={onCerrar}>Cancelar</button>
          <button
            className="btn-primary"
            onClick={() => { if (nombre.trim()) onGuardar(nombre.trim()) }}
          >
            Crear columna
          </button>
        </div>
      </div>
    </div>
  )
}
