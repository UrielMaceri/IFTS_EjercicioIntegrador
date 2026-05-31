export const API_BASE = 'http://localhost:8000'

export async function apiFetch(path, options = {}) {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  })
  if (!res.ok) {
    let detail = `Error ${res.status}`
    try {
      const data = await res.json()
      detail = data.detail ?? data.mensaje ?? detail
      if (Array.isArray(detail)) detail = detail.map(d => d.msg).join(', ')
    } catch { /* respuesta no JSON */ }
    throw new Error(detail)
  }
  if (res.status === 204) return null
  return res.json()
}
