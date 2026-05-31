import { useState, useEffect, useCallback } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import toast from 'react-hot-toast'
import '../App.css'
import './styles/KanbanBoard.css'
import './styles/NavBar.css'

import NavBar            from './components/NavBar'
import EstadoColumna     from './components/EstadoColumna'
import TareaModal        from './components/TareaModal'
import TareaDetalleModal from './components/TareaDetalleModal'
import EstadoModal       from './components/EstadoModal'

import { cargarTableroCompleto } from '../api/cargarTablero'
import { crearEstado, actualizarEstado, eliminarEstado } from '../api/estadoApi'
import { crearTarea, actualizarTarea, moverTarea, eliminarTarea } from '../api/tareaApi'
import { crearComentario, actualizarComentario, eliminarComentario } from '../api/comentarioApi'
import { cargarComentariosDeTarea } from '../api/comentarios'
import { prioridadToApi } from '../api/prioridad'


export default function KanbanBoard() {
  const navigate = useNavigate()
  const { tableroId } = useParams()

  const [nombreTablero, setNombreTablero] = useState('')
  const [estados, setEstados] = useState([])
  const [modal, setModal] = useState(null)
  const [cargando, setCargando] = useState(true)

  const usuario = JSON.parse(localStorage.getItem('usuario') ?? 'null')
  const usuarioId = usuario?.id

  const recargarTablero = useCallback(async (mostrarCarga = false) => {
    if (!tableroId) return
    if (mostrarCarga) setCargando(true)
    try {
      const { tablero, estados: lista } = await cargarTableroCompleto(tableroId)
      setNombreTablero(tablero.nombre)
      setEstados(lista)
    } catch (err) {
      toast.error(err.message ?? 'No se pudo cargar el tablero')
      navigate('/Home')
    } finally {
      if (mostrarCarga) setCargando(false)
    }
  }, [tableroId, navigate])

  useEffect(() => {
    if (!usuarioId) {
      navigate('/')
      return
    }
    if (!tableroId) {
      navigate('/Home')
      return
    }
    recargarTablero(true)
  }, [usuarioId, tableroId, navigate, recargarTablero])

  if (!usuarioId) return null

  const handleMover = async (tareaId, origenId, destinoId) => {
    try {
      await moverTarea(tareaId, destinoId)
      setEstados(prev => {
        const tarea = prev.find(e => e.id === origenId)?.tareas.find(t => t.id === tareaId)
        if (!tarea) return prev
        return prev.map(e => {
          if (e.id === origenId) return { ...e, tareas: e.tareas.filter(t => t.id !== tareaId) }
          if (e.id === destinoId) return { ...e, tareas: [...e.tareas, tarea] }
          return e
        })
      })
    } catch (err) {
      toast.error(err.message ?? 'No se pudo mover la tarea')
    }
  }

  const handleEliminar = async (tareaId, estadoId) => {
    try {
      await eliminarTarea(tareaId)
      setEstados(prev =>
        prev.map(e =>
          e.id === estadoId ? { ...e, tareas: e.tareas.filter(t => t.id !== tareaId) } : e
        )
      )
      toast.success('Tarea eliminada')
    } catch (err) {
      toast.error(err.message ?? 'No se pudo eliminar la tarea')
    }
  }

  const handleGuardarTarea = async (datos, estadoId, tareaId) => {
    try {
      if (tareaId) {
        const tareaActual = estados.flatMap(e => e.tareas).find(t => t.id === tareaId)
        await actualizarTarea(tareaId, {
          titulo: datos.titulo,
          descripcion: datos.descripcion,
          prioridad: prioridadToApi(datos.prioridad),
          fecha_vencimiento: tareaActual?.fechaVencimiento ?? new Date().toISOString(),
          posicion: tareaActual?.posicion ?? 0,
        })
        setEstados(prev =>
          prev.map(e => ({
            ...e,
            tareas: e.tareas.map(t =>
              t.id === tareaId ? { ...t, ...datos } : t
            ),
          }))
        )
        toast.success('Tarea actualizada')
      } else {
        const cantidad = estados.find(e => e.id === estadoId)?.tareas.length ?? 0
        await crearTarea({
          titulo: datos.titulo,
          descripcion: datos.descripcion,
          prioridad: prioridadToApi(datos.prioridad),
          id_estado: estadoId,
          id_usuario_asignado: usuarioId,
          fecha_vencimiento: new Date().toISOString(),
          posicion: cantidad,
        })
        await recargarTablero(false)
        toast.success('Tarea creada')
      }
      setModal(null)
    } catch (err) {
      toast.error(err.message ?? 'No se pudo guardar la tarea')
    }
  }

  const handleAgregarEstado = async (nombre) => {
    try {
      await crearEstado({
        nombre,
        posicion: estados.length,
        id_tablero: Number(tableroId),
      })
      await recargarTablero(false)
      setModal(null)
      toast.success('Columna creada')
    } catch (err) {
      toast.error(err.message ?? 'No se pudo crear la columna')
    }
  }

  const totalTareas = estados.reduce((acc, e) => acc + e.tareas.length, 0)

  const actualizarComentariosTarea = (tareaId, comentarios) => {
    setEstados(prev =>
      prev.map(e => ({
        ...e,
        tareas: e.tareas.map(t =>
          t.id === tareaId ? { ...t, comentarios } : t
        ),
      }))
    )
    setModal(m => {
      if (m?.tipo !== 'detalle' || m.tarea?.id !== tareaId) return m
      return { ...m, tarea: { ...m.tarea, comentarios } }
    })
  }

  const handleAgregarComentario = async (tareaId, contenido) => {
    await crearComentario({
      id_tarea: tareaId,
      id_usuario: usuarioId,
      contenido,
    })
    const comentarios = await cargarComentariosDeTarea(tareaId)
    actualizarComentariosTarea(tareaId, comentarios)
    toast.success('Comentario agregado')
  }

  const handleEditarComentario = async (tareaId, idComentario, contenido) => {
    await actualizarComentario(idComentario, {
      contenido,
      id_usuario_mod: usuarioId,
    })
    const comentarios = await cargarComentariosDeTarea(tareaId)
    actualizarComentariosTarea(tareaId, comentarios)
    toast.success('Comentario actualizado')
  }

  const handleEliminarComentario = async (tareaId, idComentario) => {
    await eliminarComentario(idComentario)
    const comentarios = await cargarComentariosDeTarea(tareaId)
    actualizarComentariosTarea(tareaId, comentarios)
    toast.success('Comentario eliminado')
  }

  const handleMoverEstado = async (estadoId, direccion) => {
    const idx = estados.findIndex(e => e.id === estadoId)
    const swapIdx = direccion === 'izq' ? idx - 1 : idx + 1
    if (idx < 0 || swapIdx < 0 || swapIdx >= estados.length) return

    const actual = estados[idx]
    const vecino = estados[swapIdx]
    try {
      await actualizarEstado(actual.id, { nombre: actual.nombre, posicion: vecino.posicion })
      await actualizarEstado(vecino.id, { nombre: vecino.nombre, posicion: actual.posicion })
      await recargarTablero(false)
    } catch (err) {
      toast.error(err.message ?? 'No se pudo reordenar la columna')
    }
  }

  const handleEliminarEstado = async (estado) => {
    if (estado.tareas.length > 0) {
      toast.error('Eliminá o mové las tareas antes de borrar la columna')
      return
    }
    if (!window.confirm(`¿Eliminar la columna "${estado.nombre}"?`)) return

    try {
      await eliminarEstado(estado.id)
      await recargarTablero(false)
      toast.success('Columna eliminada')
    } catch (err) {
      toast.error(err.message ?? 'No se pudo eliminar la columna')
    }
  }

  const tareaEnModal = modal?.tarea
    ? estados.flatMap(e => e.tareas).find(t => t.id === modal.tarea.id) ?? modal.tarea
    : null

  if (cargando) {
    return (
      <div className="app-layout kanban-root">
        <NavBar />
        <div className="app-main kanban-cargando">
          <p>Cargando tablero...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="app-layout kanban-root">
      <NavBar />

      <div className="app-main">
        <header className="kanban-page-header">
          <div>
            <span className="header-tablero-label">Tablero</span>
            <h1 className="header-tablero-nombre">{nombreTablero}</h1>
          </div>
          <div className="kanban-header-stats">
            <span className="header-stat">
              <span className="header-stat-num">{estados.length}</span> columnas
            </span>
            <span className="header-stat">
              <span className="header-stat-num">{totalTareas}</span> tareas
            </span>
          </div>
        </header>

        <main className="kanban-board">
          {estados.map((estado, indice) => (
            <EstadoColumna
              key={estado.id}
              estado={estado}
              estados={estados}
              indice={indice}
              onAgregarTarea={(estadoId) => setModal({ tipo: 'tarea', estadoId })}
              onMover={handleMover}
              onEliminar={handleEliminar}
              onEditar={(tarea, estadoId) => setModal({ tipo: 'tarea', estadoId, tarea })}
              onVerDetalle={(tarea, estadoId) => setModal({ tipo: 'detalle', estadoId, tarea })}
              onMoverEstado={handleMoverEstado}
              onEliminarEstado={handleEliminarEstado}
            />
          ))}

          <button className="btn-agregar-columna" onClick={() => setModal({ tipo: 'estado' })}>
            <span className="plus-icon">+</span>
            <span>Nueva columna</span>
          </button>
        </main>
      </div>

      {modal?.tipo === 'detalle' && tareaEnModal && (
        <TareaDetalleModal
          tarea={tareaEnModal}
          usuarioId={usuarioId}
          onCerrar={() => setModal(null)}
          onAgregarComentario={handleAgregarComentario}
          onEditarComentario={handleEditarComentario}
          onEliminarComentario={handleEliminarComentario}
          onEditar={(tarea) => setModal({ tipo: 'tarea', estadoId: modal.estadoId, tarea })}
        />
      )}
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
