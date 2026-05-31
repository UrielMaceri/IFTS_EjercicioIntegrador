const A_API = { alta: 3, media: 2, baja: 1 }
const DE_API = { 1: 'baja', 2: 'media', 3: 'alta' }

export function prioridadToApi(prioridad) {
  return A_API[prioridad] ?? 2
}

export function prioridadFromApi(prioridad) {
  return DE_API[prioridad] ?? 'media'
}
