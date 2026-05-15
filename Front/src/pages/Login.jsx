import '../App.css'
import { useNavigate } from "react-router-dom"

export default function Login() {

    const objeto = {nombre: "Login.jsx"}
    const navigate = useNavigate()

    return(
    <div id="center">
        

        <section>
            <h1>Login</h1>
            <br />
            <input type="text" placeholder="Usuario" />
            <br />
            <input type="password" placeholder="Contraseña" />
            <br />
            <br />
            <button
                type="button"
                height="40px"
                className="counter"
                onClick={() => navigate("/Home")}
                >Iniciar sesión
            </button>            
        </section>

        <footer id='footer-fixed'>{objeto.nombre}</footer>
    </div>
    )
}