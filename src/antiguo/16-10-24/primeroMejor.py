from claseBusqueda import Busqueda
from claseColas import ColaHeuristica
#Para analiticas de ver cuanto tarda en ejecutarse
import time
start = time.time()

heuristica = ColaHeuristica()

class BusquedaPM(Busqueda):
    def __init__(self, cerrados = set()):
        super().__init__(cerrados)
    #deberia usarse la velocidad máxima tb (accion.maxSpeed)
    #PREGUNTA: Al ser la misma vel para todos, a la hora de comparar
    # caminos para elegir no se va a alterar el camino elegido. Pues son
    # todos proporcionales divididos por el mismo numero.
    def seleccionSiguienteNodo(self, frontera):
        return heuristica.getLeastDistance(frontera)

print(f"\nBusqueda Primero Mejor:\n")
fin = BusquedaPM().bus()
for i in fin:
    print(i)
print(f"\nFIN DEL ALGORITMO")

end = time.time()
print("Tiempo de ejecución :",(end-start) * 10**3, "ms")