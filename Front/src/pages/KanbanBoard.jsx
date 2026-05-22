import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import '../App.css'
import './styles/KanbanBoard.css'

import EstadoColumna from './components/EstadoColumna'
import TareaModal    from './components/TareaModal'
import EstadoModal   from './components/EstadoModal'


export default function KanbanBoard() {
  const navigate = useNavigate()
  const nombreTablero = 'Tablero Principal'

  const [estados, setEstados] = useState([])
  const [modal, setModal] = useState(null)  // { tipo: 'tarea'|'estado', estadoId?, tarea? }

  // Mover tarea entre estados
  const handleMover = (tareaId, origenId, destinoId) => {
    setEstados(prev => {
      const tarea = prev.find(e => e.id === origenId)?.tareas.find(t => t.id === tareaId)
      if (!tarea) return prev
      return prev.map(e => {
        if (e.id === origenId)  return { ...e, tareas: e.tareas.filter(t => t.id !== tareaId) }
        if (e.id === destinoId) return { ...e, tareas: [...e.tareas, tarea] }
        return e
      })
    })
  }

  // Eliminar tarea
  const handleEliminar = (tareaId, estadoId) => {
    setEstados(prev =>
      prev.map(e =>
        e.id === estadoId ? { ...e, tareas: e.tareas.filter(t => t.id !== tareaId) } : e
      )
    )
  }

  // Guardar tarea (nueva o editada)
  const handleGuardarTarea = (datos, estadoId, tareaId) => {
    setEstados(prev =>
      prev.map(e => {
        if (e.id !== estadoId) return e
        if (tareaId) {
          return { ...e, tareas: e.tareas.map(t => t.id === tareaId ? { ...t, ...datos } : t) }
        }
        return { ...e, tareas: [...e.tareas, { id: Date.now(), ...datos }] }
      })
    )
    setModal(null)
  }

  // Agregar nuevo estado
  const handleAgregarEstado = (nombre, color) => {
    setEstados(prev => [...prev, { id: Date.now(), nombre, color, tareas: [] }])
    setModal(null)
  }

  const totalTareas = estados.reduce((acc, e) => acc + e.tareas.length, 0)

  return (
    <div className="kanban-root">
      <header id="header-fixed">
        <div className="header-left">
          <span className="header-tablero-label">Tablero</span>
          <span className="header-tablero-nombre">{nombreTablero}</span>
        </div>
        <div>
          <button type="button"
           className="counter" 
           onClick={() => navigate('/Home')}>
            Menu Principal
          </button>
        </div>
        <div className="margin-right">
          <button type="button"
           className="counter" 
           onClick={() => navigate('/')}>
            Salir
          </button>
        </div>
      </header>

      <main className="kanban-board">
        {estados.map(estado => (
          <EstadoColumna
            key={estado.id}
            estado={estado}
            estados={estados}
            onAgregarTarea={(estadoId) => setModal({ tipo: 'tarea', estadoId })}
            onMover={handleMover}
            onEliminar={handleEliminar}
            onEditar={(tarea, estadoId) => setModal({ tipo: 'tarea', estadoId, tarea })}
          />
        ))}

        <button className="btn-agregar-columna" onClick={() => setModal({ tipo: 'estado' })}>
          <span className="plus-icon">+</span>
          <span>Nueva columna</span>
        </button>
      </main>

      <footer id="footer-fixed">KanbanBoard.jsx</footer>

      {modal?.tipo === 'tarea' && (
        <TareaModal
          estadoId={modal.estadoId}
          tarea={modal.tarea ?? null}
          onGuardar={handleGuardarTarea}
          onCerrar={() => setModal(null)}
        />
      )}
      {modal?.tipo === 'estado' && (
        <EstadoModal
          onGuardar={handleAgregarEstado}
          onCerrar={() => setModal(null)}
        />
      )}
    </div>
  )
}
