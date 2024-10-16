from claseBusqueda import Busqueda
#Para analiticas de ver cuanto tarda en ejecutarse
import time
start = time.time()

class BusquedaAnchura(Busqueda):
    def __init__(self, cerrados = set()):
        super().__init__(cerrados)

    def seleccionSiguienteNodo(self, frontera):
        return frontera[0]

print(f"\nBusqueda en Anchura:\n")
fin = BusquedaAnchura().bus()
for i in fin:
    print(i)
print(f"\nFIN DEL ALGORITMO")

end = time.time()
print("Tiempo de ejecución :",(end-start) * 10**3, "ms")