import '../App.css'
import './styles/Login.css'
import { useNavigate } from "react-router-dom"
import { useState } from 'react'
import { FiEye, FiEyeOff } from 'react-icons/fi'

export default function Login() {

    const objeto = {nombre: "Login.jsx"}
    const navigate = useNavigate()
    const [verPassword, setVerPassword] = useState(false) 

    return(
    <div id="center">
        
        <section className="login-form">
            <h1>Login</h1>
            <br />

            <div className="form-row">
                <input id="usuario" type="text" placeholder="E-Mail" />
            </div>

            <div className="form-row">
                <div className="login-password-wrapper">
                    <input
                        id="password"
                        type={verPassword ? "text" : "password"}
                        placeholder="Contraseña"
                    />
                    <button
                        type="button"
                        onClick={() => setVerPassword(v => !v)}
                        className="toggle-password"
                        aria-label={verPassword ? "Ocultar contraseña" : "Mostrar contraseña"}
                    >
                        {verPassword ? <FiEyeOff size={20} /> : <FiEye size={20} />}
                    </button>
                </div>
            </div>
            <br />
            <div>
                <button
                    type="button"
                    className="counter button-margin"
                    onClick={() => navigate("/Home")}
                    >Iniciar sesión
                </button>
                <button
                    type="button"
                    className="counter"
                    onClick={() => navigate("/Register")}
                    >Registrarse
                </button>
            </div>
        </section>

        <footer id='footer-fixed'>{objeto.nombre}</footer>
    </div>
    )
}