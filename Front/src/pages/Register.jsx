import '../App.css'
import './styles/Register.css'
import { useState } from 'react'
import { FiEye, FiEyeOff } from 'react-icons/fi'
import { useNavigate } from "react-router-dom"

export default function Register() {

    const objeto = {nombre: "Register.jsx"}
    const [verPassword, setVerPassword] = useState(false) 
    const navigate = useNavigate()

    return(
    <div id="center">
        <header id='header-fixed' >
            <div className='header-left'>
            </div> 
            <div className='header-right'>
                <button
                    type="button"
                    className="counter"
                    onClick={() => navigate("/")}
                    >Salir
                </button>
            </div>   
        </header>

        <h1>Introduzca sus datos</h1>
        <br />

        <section className="register-form">  
            {/* NOMBRE*/}
            <div className="form-row">
                <label className="field-desc" htmlFor="nombre">Nombre:</label>
                <input id="nombre" className="field-input" type="text" />
            </div>

            {/* APELIDO*/}
            <div className="form-row">
                <label className="field-desc" htmlFor="apellido">Apellido:</label>
                <input id="apellido" type="text" />
            </div>

            {/* MAIL*/}
            <div className="form-row">
                <label className="field-desc" htmlFor="mail">E-Mail:</label>
                <input id="mail" type="text" />
            </div>

            {/* CONTRASEÑA*/}
            <div className="form-row">
                <label className="field-desc" htmlFor="password">Contraseña:</label>
                <div className="password-wrapper">
                    <input id="password" type={verPassword ? "text" : "password"} />
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

        </section>
        
        <br />
        <button type="button" className="counter big-button">Registrarse</button>

        <footer id='footer-fixed'>{objeto.nombre}</footer>
    </div>
    )
}