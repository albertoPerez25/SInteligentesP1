import heapq
from claseBusqueda import Busqueda
from claseColas import ColaHeuristica
#Para analiticas de ver cuanto tarda en ejecutarse
import time
start = time.time()

heuristica = ColaHeuristica()

class BusquedaPM(Busqueda):
    def __init__(self, cerrados = set()):
        super().__init__(cerrados)
    
    def añadir(self, nodo, pq = None):
        if pq == None:
            pq = self.frontera
        
        heapq.heappush(pq,(nodo.getDistanceToFinal(nodo) / nodo.getSpeedOf(nodo.accion),nodo))
        return pq

print(f"\nBusqueda Primero Mejor:\n")
fin = BusquedaPM().bus()
for i in fin:
    print(i)
print(f"\nFIN DEL ALGORITMO")

end = time.time()
print("Tiempo de ejecución :",(end-start) * 10**3, "ms")