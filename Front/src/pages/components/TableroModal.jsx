import { useState } from 'react'
import '../styles/KanbanBoard.css'

export default function TableroModal({ onGuardar, onCerrar }) {
  const [nombre, setNombre] = useState('')
  const [descripcion, setDescripcion] = useState('')

  const handleGuardar = () => {
    if (!nombre.trim()) return
    onGuardar(nombre.trim(), descripcion.trim())
  }

  return (
    <div className="modal-overlay" onClick={onCerrar}>
      <div className="modal-box modal-box--sm" onClick={e => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Nuevo tablero</h2>
          <button type="button" className="btn-icon modal-close" onClick={onCerrar}>✕</button>
        </div>

        <div className="modal-body">
          <label>Nombre</label>
          <input
            className="modal-input"
            type="text"
            value={nombre}
            onChange={e => setNombre(e.target.value)}
            autoFocus
          />

          <label>Descripción</label>
          <textarea
            className="modal-input modal-textarea"
            value={descripcion}
            onChange={e => setDescripcion(e.target.value)}
            rows={3}
          />
        </div>

        <div className="modal-footer">
          <button type="button" className="btn-secondary" onClick={onCerrar}>Cancelar</button>
          <button type="button" className="btn-primary" onClick={handleGuardar} disabled={!nombre.trim()}>
            Crear tablero
          </button>
        </div>
      </div>
    </div>
  )
}
