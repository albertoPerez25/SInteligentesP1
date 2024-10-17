from clasesBasicas import problema,Nodo
from claseBusqueda import Busqueda

class ColaHeuristica:
    def __init__(self, frontera = set()):
        self.frontera = frontera
        self.diccionario = None  

    def getLeastDistance(self, frontera):
        dist = 999999999
        aux = 0
        sol = None
        for nodo in frontera:
            aux = Nodo.getDistanceToFinal(nodo) * problema.maxSpeed #Han dicho en clase de usar velocidad. No le veo sentido 
            if (aux < dist):
                dist = aux
                sol = nodo
        return sol

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
