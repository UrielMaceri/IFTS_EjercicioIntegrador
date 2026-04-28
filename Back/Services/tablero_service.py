from Classes.tablero import Tablero
from Classes.estado import Estado

class TableroService:
    #def __init__(self, tablero_repository):
        #self.tablero_repository = tablero_repository
    
    def reordenar_estado(self, tablero: Tablero, estado_id: int, nueva_posicion: int):

        estado_a_mover = next((e for e in tablero.estados if e.id == estado_id), None)
        
        if estado_a_mover:
            tablero.estados.remove(estado_a_mover)
            tablero.estados.insert(nueva_posicion, estado_a_mover)
        
            for i, estado in enumerate(tablero.estados):
                estado.posicion = i
        else:
            print(f"Estado con ID {estado_id} no encontrado en el tablero.")