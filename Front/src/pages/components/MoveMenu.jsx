import { useEffect, useRef, useState } from 'react'
import { createPortal } from 'react-dom'

export default function MoveMenu({ isOpen, buttonRef, estados, estadoId, tarea, onMover, onClose }) {
  const [position, setPosition] = useState({ top: 0, left: 0 })
  const menuRef = useRef(null)

  useEffect(() => {
    if (isOpen && buttonRef?.current) {
      const rect = buttonRef.current.getBoundingClientRect()
      setPosition({
        top: rect.top - 8,
        left: rect.right - 150,
      })

      // Cerrar si se hace click fuera
      const handleClickOutside = (e) => {
        if (menuRef.current && !menuRef.current.contains(e.target) && !buttonRef.current.contains(e.target)) {
          onClose()
        }
      }

      document.addEventListener('mousedown', handleClickOutside)
      return () => document.removeEventListener('mousedown', handleClickOutside)
    }
  }, [isOpen, buttonRef, onClose])

  if (!isOpen) return null

  return createPortal(
    <div
      ref={menuRef}
      className="move-menu"
      style={{
        top: `${position.top}px`,
        left: `${position.left}px`,
      }}
    >
      {estados
        .filter(e => e.id !== estadoId)
        .map(e => (
          <button
            key={e.id}
            type="button"
            onClick={() => {
              onMover(tarea.id, estadoId, e.id)
              onClose()
            }}
          >
            <span className="move-dot" style={{ background: e.color }} />
            {e.nombre}
          </button>
        ))}
    </div>,
    document.body
  )
}
