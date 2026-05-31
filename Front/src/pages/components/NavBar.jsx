import { useEffect, useState, useCallback } from 'react'
import { useNavigate, useLocation, useParams } from 'react-router-dom'
import toast from 'react-hot-toast'
import { obtenerTablerosPorUsuario, crearTablero, eliminarTablero } from '../../api/tableroApi'
import { limpiarCacheUsuarios } from '../../api/usuarioApi'
import TableroModal from './TableroModal'
import logoNavbar from '../../assets/drake.png'
import '../styles/NavBar.css'

export default function NavBar() {
  const navigate = useNavigate()
  const location = useLocation()
  const { tableroId } = useParams()
  const usuario = JSON.parse(localStorage.getItem('usuario') ?? 'null')

  const [tableros, setTableros] = useState([])
  const [cargandoTableros, setCargandoTableros] = useState(true)
  const [modalTablero, setModalTablero] = useState(false)

  const recargarTableros = useCallback(async () => {
    if (!usuario?.id) return
    setCargandoTableros(true)
    try {
      const data = await obtenerTablerosPorUsuario(usuario.id)
      setTableros(data)
    } catch (err) {
      toast.error(err.message ?? 'No se pudieron cargar los tableros')
    } finally {
      setCargandoTableros(false)
    }
  }, [usuario?.id])

  useEffect(() => {
    recargarTableros()
  }, [recargarTableros])

  const cerrarSesion = () => {
    localStorage.removeItem('usuario')
    limpiarCacheUsuarios()
    navigate('/')
  }

  const handleEliminarTablero = async (tablero, e) => {
    e.stopPropagation()
    if (!window.confirm(`¿Eliminar el tablero "${tablero.nombre}"? Se borrarán sus columnas y tareas.`)) return

    try {
      await eliminarTablero(tablero.id)
      const lista = await obtenerTablerosPorUsuario(usuario.id)
      setTableros(lista)
      toast.success('Tablero eliminado')

      if (tableroActivoId === tablero.id) {
        navigate(lista.length > 0 ? `/board/${lista[0].id}` : '/Home')
      }
    } catch (err) {
      toast.error(err.message ?? 'No se pudo eliminar el tablero')
    }
  }

  const handleCrearTablero = async (nombre, descripcion) => {
    try {
      await crearTablero({
        nombre,
        descripcion: descripcion || 'Sin descripción',
        id_propietario: usuario.id,
      })
      const lista = await obtenerTablerosPorUsuario(usuario.id)
      setTableros(lista)
      setModalTablero(false)
      toast.success('Tablero creado')

      if (lista.length > 0) {
        const nuevo = lista.reduce((a, b) => (a.id > b.id ? a : b))
        navigate(`/board/${nuevo.id}`)
      }
    } catch (err) {
      toast.error(err.message ?? 'No se pudo crear el tablero')
    }
  }

  const nombreUsuario = usuario?.nombre ?? usuario?.mail ?? 'Usuario'
  const enInicio = location.pathname === '/Home'
  const tableroActivoId = tableroId ? Number(tableroId) : null

  return (
    <>
      <nav className="app-navbar" aria-label="Navegación principal">
        <div className="navbar-brand">
          <img className="navbar-brand-icon" src={logoNavbar} alt="" aria-hidden="true" />
          <div>
            <p className="navbar-app">UriGami</p>
            <p className="navbar-sub">Gestión de tareas</p>
          </div>
        </div>

        <ul className="navbar-links">
          <li>
            <button
              type="button"
              className={`navbar-link ${enInicio ? 'active' : ''}`}
              onClick={() => navigate('/Home')}
            >
              Inicio
            </button>
          </li>
        </ul>

        <div className="navbar-tableros">
          <div className="navbar-tableros-header">
            <p className="navbar-seccion-titulo">Mis tableros</p>
            <button
              type="button"
              className="navbar-btn-nuevo"
              onClick={() => setModalTablero(true)}
              title="Crear tablero"
            >
              +
            </button>
          </div>
          {cargandoTableros && (
            <p className="navbar-tableros-estado">Cargando...</p>
          )}
          {!cargandoTableros && tableros.length === 0 && (
            <p className="navbar-tableros-estado">No tenés tableros todavía.</p>
          )}
          <ul className="navbar-tableros-lista">
            {tableros.map(t => (
              <li key={t.id} className="navbar-tablero-item">
                <button
                  type="button"
                  className={`navbar-tablero-link ${tableroActivoId === t.id ? 'active' : ''}`}
                  onClick={() => navigate(`/board/${t.id}`)}
                  title={t.descripcion || t.nombre}
                >
                  <span className="navbar-tablero-nombre">{t.nombre}</span>
                </button>
                <button
                  type="button"
                  className="navbar-tablero-eliminar"
                  title="Eliminar tablero"
                  onClick={(e) => handleEliminarTablero(t, e)}
                >
                  ✕
                </button>
              </li>
            ))}
          </ul>
        </div>

        <div className="navbar-footer">
          <div className="navbar-user" title={usuario?.mail}>
            <span className="navbar-avatar">{nombreUsuario.charAt(0).toUpperCase()}</span>
            <span className="navbar-user-name">{nombreUsuario}</span>
          </div>
          <button type="button" className="navbar-logout" onClick={cerrarSesion}>
            Cerrar sesión
          </button>
        </div>
      </nav>

      {modalTablero && (
        <TableroModal
          onGuardar={handleCrearTablero}
          onCerrar={() => setModalTablero(false)}
        />
      )}
    </>
  )
}
