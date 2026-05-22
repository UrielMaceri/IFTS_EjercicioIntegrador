import '../App.css'
import { useNavigate } from "react-router-dom"

export default function Home() {

    const objeto = {nombre: "Home.jsx"}
    const navigate = useNavigate()
    
    return (
    <div id="center">
        <header id='header-fixed'>
            <button
                type="button"
                className="counter"
                onClick={() => navigate("/")}
                >Cerrar Sesión
            </button>   
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
                // onClick={() => }
                >Prueba de botón Home
            </button>
        </section>

        <footer id='footer-fixed'>{objeto.nombre}</footer>
    </div>)
};