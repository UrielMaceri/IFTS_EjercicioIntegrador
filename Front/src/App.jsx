import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'

import Home from "./pages/Home.jsx"
import Login from "./pages/Login.jsx"
import Register from "./pages/Register.jsx"
import KanbanBoard from "./pages/KanbanBoard.jsx"

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/Register" element={<Register />} />
          <Route path="/Home" element={<Home />} />
          <Route path="/board" element={<KanbanBoard />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
