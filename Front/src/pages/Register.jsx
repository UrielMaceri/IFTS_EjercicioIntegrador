import '../App.css'
import './styles/Register.css'
import { useState } from 'react'
import { FiEye, FiEyeOff } from 'react-icons/fi'
import { useNavigate } from "react-router-dom"
import toast from 'react-hot-toast'

export default function Register() {

    const objeto = {nombre: "Register.jsx"}
    const [verPassword, setVerPassword] = useState(false) 
    const navigate = useNavigate()

    // Estados de campos 
    const [nombre, setNombre] = useState('')
    const [apellido, setApellido] = useState('')
    const [mail, setMail] = useState('')
    const [contrasena, setContrasena] = useState('')
    const [error, setError] = useState('')
    const errorForm = 0

    const handleSubmit = async () => {
        if (nombre.trim() === ''){
            toast.error('El nombre no puede estar vacío')
            return
        }
        if (apellido.trim() === '') {
            toast.error('El apellido no puede estar vacío')
            return
        }
        if (!mail.includes('@')) {
            toast.error('El mail no es válido')
            return
        }
        if (contrasena.length < 8) {
            toast.error('La contraseña debe tener al menos 8 caracteres')
            return
        }
        const response = await fetch('http://localhost:8000/usuario/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nombre, apellido, mail, contrasena})
            })
        if (response.ok) {
            toast.success('Usuario registrado correctamente')
            navigate('/')
        } else {
            const data = await response.json()
            setError(data.detail)
        }
    }

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
                <input id="nombre" className="field-input" type="text"
                value={nombre}
                onChange={e => setNombre(e.target.value)}/>
            </div>

            {/* APELIDO*/}
            <div className="form-row">
                <label className="field-desc" htmlFor="apellido">Apellido:</label>
                <input id="apellido" type="text" 
                value={apellido}
                onChange={e => setApellido(e.target.value)}/>
            </div>

            {/* MAIL*/}
            <div className="form-row">
                <label className="field-desc" htmlFor="mail">E-Mail:</label>
                <input id="mail" type="text" 
                value={mail}
                onChange={e => setMail(e.target.value)}/>
            </div>

            {/* CONTRASEÑA*/}
            <div className="form-row">
                <label className="field-desc" htmlFor="password">Contraseña:</label>
                <div className="password-wrapper">
                    <input id="password" type={verPassword ? "text" : "password"} 
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

        </section>
        
        <br />
        <button type="button" 
        className="counter big-button" 
        onClick={handleSubmit}
        >Registrarse</button>

        <footer id='footer-fixed'>{objeto.nombre}</footer>
    </div>
    )
}