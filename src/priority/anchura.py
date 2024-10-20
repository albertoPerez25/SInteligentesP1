from claseBusqueda import Busqueda
import heapq
#Para analiticas de ver cuanto tarda en ejecutarse
import time
start = time.time()

class BusquedaAnchura(Busqueda):
    def __init__(self, cerrados = set()):
        super().__init__(cerrados)
    
    def añadir(self, nodo, pq = None):
        if pq == None:
            pq = self.frontera
        
        heapq.heappush(pq,(nodo.getIntersectionId(),nodo))
        return pq

print(f"\nBusqueda en Anchura:\n")
fin = BusquedaAnchura().bus()
for i in fin:
    print(i)
print(f"\nFIN DEL ALGORITMO")

end = time.time()
print("Tiempo de ejecución :",(end-start) * 10**3, "ms")