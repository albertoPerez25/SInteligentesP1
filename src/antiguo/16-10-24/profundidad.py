from claseBusqueda import Busqueda
#Para analiticas de ver cuanto tarda en ejecutarse
import time
start = time.time()
class BusquedaProfundidad(Busqueda):
    def __init__(self, cerrados = set()):
        super().__init__(cerrados)
    def seleccionSiguienteNodo(self, frontera):
        for i in frontera:
            nodo=i
        return nodo
print(f"\nBusqueda en Profundidad:\n")
nodos=BusquedaProfundidad().bus()
for i in nodos:
    print (i)
print(f"\nFIN DEL ALGORITMO")
end = time.time()
print("Tiempo de ejecución :",(end-start) * 10**3, "ms")