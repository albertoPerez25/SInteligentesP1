from cargadorjson import nodoaux,problema

#Para analiticas de ver cuanto tarda en ejecutarse
import time
start = time.time()
 

class Nodo:
    def __init__(self, interseccion, padre = None, accion = None, coste = 0, profundidad = 0):
        self.estado = interseccion
        self.padre = padre
        self.accion = accion
        self.coste = coste
        self.profundidad = profundidad

        #Lista de calles de la interseccion
        self.calles = nodoaux.getSegmentsOf(nodoaux.getIntersectionId(self.estado))
        self.it = 0 #Iterador para self.calles
        
    def __str__(self):
        return f"Nodo(estado={self.estado}, padre={self.padre}, accion={self.accion}, coste={self.coste}, profundidad={self.profundidad})"

    #Devuelve la siguiente calle de la interseccion
    def getNextSegment(self,segments = []):
        if (len(segments) == 0):
            segments = self.calles
        if (self.it >= len(segments)):
            return None
        segment = segments[self.it]
        self.it = self.it + 1
        return segment

class Estado:
    def __init__(self,problema):
        self.nodo = problema

def Sucesor(problema, estado):
    ret = set()
    while True:
        accion = estado.getNextSegment() #es uno de los segmentos de la interseccion en el nodo estado
        if (accion == None):
            return ret
        sucesor = nodoaux.getDestinationOf(accion) #es la interseccion destino de accion
        tupla = (accion, sucesor)
        ret.add(tupla)

def testObjetivo(nodo,problema):
    return nodoaux.getIntersectionId(nodo.estado) == problema["final"]

def costeIndividual(origen,calle,destino):
    return nodoaux.getDistanceOf(calle) / nodoaux.getSpeedOf(calle)

def listaSolucion(nodo):
    sol = []
    aux = nodo
    while (aux.padre):
        sol.append(aux.estado)
        aux = aux.padre
    sol.append(aux.estado)
    return sol

visitados = set() #para no volver a expandir nodos ya visitados

def expandir(nodo,problema):
    sucesores = []
    for (accion,resultado) in Sucesor(problema,nodo):
        if (not (nodoaux.getIntersectionId(resultado) in visitados)):
            s = Nodo(resultado, nodo, accion)
            s.coste = nodo.coste + costeIndividual(nodo,accion,s)
            s.profundidad = nodo.profundidad + 1
            sucesores.append(s)
    return sucesores

def busquedaArbol(problema,frontera):
    estado = Estado(nodoaux.getIntersection(problema["inicial"]))
    nodo = Nodo(estado.nodo)
    frontera.add(nodo)
    while(True):
        nodo = next(iter(frontera))
        visitados.add(nodoaux.getIntersectionId(nodo.estado))
        if (len(frontera) == 0):
            return Exception
        frontera.remove(nodo)
        if (testObjetivo(nodo,problema)):
            return listaSolucion(nodo)
        nose = expandir(nodo,problema)
        frontera = frontera.union(nose)

fin = busquedaArbol(problema,set())
print(f"\nAlgoritmo de búsqueda de árbol en anchura")
print(f"Inicio: {problema["inicial"]} \nFinal: {problema["final"]}\n")
for i in fin:
    print(i)
print(f"\nFIN DEL ALGORITMO")

#POSIBLES MEJORAS:
#Añadir lista de nodos ya visitados, e impedir que se expandan de nuevo.

#Para hacer en profundidad habria que cambiar expandir y/o Sucesor para que
#devolviera solo un nodo hijo (una interseccion de todas las posibles)
#en vez de un array con todas.
#Si queremos hacer que vuelva cuando llegue a abajo del todo, se podrian
#devolver todos pero guardarlos en otra lista a parte, y cuando len(frontera) == 0
#en vez de una excepcion hacer que nodo = lista[+1] , que nodo sea el siguiente en la lista
#y se borra.

end = time.time()
print("Tiempo de ejecución :",
      (end-start) * 10**3, "ms")