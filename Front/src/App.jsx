import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'

import Home from "./pages/Home.jsx"
import Login from "./pages/Login.jsx"

function App() {
  const [count, setCount] = useState(0)

  const objeto = {nombre: "App.jsx"}

  return (
    <>
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/Home" element={<Home />} />
      </Routes>
    </BrowserRouter>
    </>
  )
}

export default App
