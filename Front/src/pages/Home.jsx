import '../App.css'
import './styles/Home.css'
import './styles/NavBar.css'
import { useNavigate } from 'react-router-dom'
import NavBar from './components/NavBar'

export default function Home() {
  const navigate = useNavigate()
  const usuario = JSON.parse(localStorage.getItem('usuario'))
  if (!usuario) navigate('/')

  const nombre = usuario?.nombre ?? usuario?.mail ?? 'Usuario'

  return (
    <div className="app-layout">
      <NavBar />

      <div className="app-main">
        <section className="home-page">
          <h1>Hola, {nombre}</h1>
          <p>Seleccioná un tablero del menú lateral para empezar a trabajar.</p>
        </section>
      </div>
    </div>
  )
}
