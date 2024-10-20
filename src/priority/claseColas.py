from clasesBasicas import problema,Nodo
from claseBusqueda import Busqueda
import heapq

class ColaHeuristica:
    def __init__(self, frontera = set()):
        self.frontera = frontera
        self.diccionario = None  
        pQueue = []
#   t=d/v
    def getLeastDistance(self, frontera):
        tiempo = 999999999
        aux = 0
        sol = None
        for nodo in frontera:
            d=Nodo.getDistanceToFinal(nodo)
            s=nodo.getSpeedOf(nodo.accion)
            aux = Nodo.getDistanceToFinal(nodo) / nodo.getSpeedOf(nodo.accion) #Cogemos la velocidad de la calle
            if (aux < tiempo):
                tiempo = aux
                sol = nodo
        return sol
    
    def getLeastDistancePriority(self, frontera):
        for nodo in frontera:
            time = Nodo.getDistanceToFinal(nodo) / nodo.getSpeedOf(nodo.accion)
            heapq.heappush(self.pQueue,(time,nodo))

    def storeDistances(self, intersections):
        for nodo in intersections:
            self.diccionario.update({"Id": Nodo.getIntersectionId(nodo),"Distancia":Nodo.getDistanceToFinal(nodo)})

    def getLeastDistanceFromStored(self, frontera):
        dist = 999999999
        sol = None
        for id,dis in self.diccionario.items():       
            if (dis < dist):
                dist = dis
                sol = id
        return problema.getIntersection(sol)
