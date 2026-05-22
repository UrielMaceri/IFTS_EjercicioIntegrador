import TareaCard from './TareaCard'

export default function EstadoColumna({ estado, onAgregarTarea, onMover, onEliminar, onEditar, estados }) {
  return (
    <div className="estado-columna">
      <div className="estado-header">
        <span className="estado-dot" style={{ background: estado.color }} />
        <h3 className="estado-nombre">{estado.nombre}</h3>
        <span className="estado-count">{estado.tareas.length}</span>
      </div>

      <div className="estado-body">
        {estado.tareas.length === 0 && (
          <div className="estado-empty">Sin tareas</div>
        )}
        {estado.tareas.map(t => (
          <TareaCard
            key={t.id}
            tarea={t}
            estadoId={estado.id}
            onMover={onMover}
            onEliminar={onEliminar}
            onEditar={onEditar}
            estados={estados}
          />
        ))}
      </div>

      <button className="btn-agregar-tarea" onClick={() => onAgregarTarea(estado.id)}>
        + Nueva tarea
      </button>
    </div>
  )
}
