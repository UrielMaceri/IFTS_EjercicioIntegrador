import TareaCard from './TareaCard'

export default function EstadoColumna({
  estado,
  estados,
  indice,
  onAgregarTarea,
  onMover,
  onEliminar,
  onEditar,
  onVerDetalle,
  onMoverEstado,
  onEliminarEstado,
}) {
  const puedeIzq = indice > 0
  const puedeDer = indice < estados.length - 1

  return (
    <div className="estado-columna">
      <div className="estado-header">
        <h3 className="estado-nombre">{estado.nombre}</h3>
        <span className="estado-count">{estado.tareas.length}</span>
        <div className="estado-header-actions">
          <button
            type="button"
            className="btn-icon"
            title="Mover a la izquierda"
            disabled={!puedeIzq}
            onClick={() => onMoverEstado(estado.id, 'izq')}
          >
            ‹
          </button>
          <button
            type="button"
            className="btn-icon"
            title="Mover a la derecha"
            disabled={!puedeDer}
            onClick={() => onMoverEstado(estado.id, 'der')}
          >
            ›
          </button>
          <button
            type="button"
            className="btn-icon btn-danger"
            title="Eliminar columna"
            onClick={() => onEliminarEstado(estado)}
          >
            ✕
          </button>
        </div>
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
            onVerDetalle={onVerDetalle}
            estados={estados}
          />
        ))}
      </div>

      <button type="button" className="btn-agregar-tarea" onClick={() => onAgregarTarea(estado.id)}>
        + Nueva tarea
      </button>
    </div>
  )
}
