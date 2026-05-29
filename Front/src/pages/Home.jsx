import '../App.css'
import './styles/Home.css'
import { useNavigate } from "react-router-dom"

export default function Home() {

    const objeto = {nombre: "Home.jsx"}
    const navigate = useNavigate()
    
    return (
    <div id="center">
        <header id='header-fixed' >
            <div className='header-left'>
            </div> 
            <div className='header-right'>
                <button
                    type="button"
                    className="counter"
                    onClick={() => 
                        {localStorage.removeItem('usuario')
                        navigate("/")}}
                    >Cerrar Sesión
                </button>
            </div>   
        </header>
        <section>
            <div>
                <h1>Pantalla principal</h1>
                <p>
                </p>
            </div>
            <br />
            <button
                type="button"
                className="counter"
                onClick={() => navigate("/board")}
                >Ir a tablero
            </button>
        </section>

        <footer id='footer-fixed'>{objeto.nombre}</footer>
    </div>)
};