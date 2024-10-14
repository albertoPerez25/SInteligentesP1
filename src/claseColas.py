from clasesBasicas import operaciones,problema,estado,accion,Nodo
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
            aux = estado.getDistanceToFinal(nodo) * accion.maxSpeed #Han dicho en clase de usar velocidad. No le veo sentido 
            if (aux < dist):
                dist = aux
                sol = nodo
        return sol

    def storeDistances(self, intersections):
        for nodo in intersections:
            self.diccionario.update({"Id": problema.getIntersectionId(nodo),"Distancia":estado.getDistanceToFinal(nodo)})

    def getLeastDistanceFromStored(self, frontera):
        dist = 999999999
        sol = None
        for id,dis in self.diccionario.items():       
            if (dis < dist):
                dist = dis
                sol = id
        return problema.getIntersection(sol)
