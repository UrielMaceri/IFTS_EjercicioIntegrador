import '../App.css'
import './styles/Login.css'
import { useNavigate } from "react-router-dom"
import { useState } from 'react'
import { FiEye, FiEyeOff } from 'react-icons/fi'
import toast from 'react-hot-toast'

export default function Login() {

    const objeto = {nombre: "Login.jsx"}
    const navigate = useNavigate()
    const [verPassword, setVerPassword] = useState(false) 

    // Estados de campos
    const [mail, setMail] = useState('')
    const [contrasena, setContrasena] = useState('')

    const handleSubmit = async () => {
        if (!mail.includes('@')) {
            toast.error('El mail no es válido')
            return
        }
        if (contrasena.length < 8) {
            toast.error('La contraseña debe tener al menos 8 caracteres')
            return
        }
        const response = await fetch('http://localhost:8000/auth/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ mail, contrasena})
            })
        if (response.ok) {
            toast.success('Login exitoso!')
            const data = await response.json()
            localStorage.setItem('usuario', JSON.stringify(data))
            navigate('/Home')
        } else {
            const data = await response.json()
            toast.error(data.detail) 
        }
    }
    
    return(
    <div id="center">
        
        <section className="login-form">
            <h1>Login</h1>
            <br />

            <div className="form-row">
                <input id="usuario" type="text" placeholder="E-Mail" 
                value={mail}
                onChange={e => setMail(e.target.value)}/>
            </div>

            <div className="form-row">
                <div className="login-password-wrapper">
                    <input
                        id="password"
                        type={verPassword ? "text" : "password"}
                        placeholder="Contraseña"
                        value={contrasena}
                        onChange={e => setContrasena(e.target.value)}/>
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
                    onClick={handleSubmit}
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