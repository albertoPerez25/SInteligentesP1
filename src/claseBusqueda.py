from clasesBasicas import operaciones,problema,estado,accion,Nodo

class Busqueda:
    def __init__(self,cerrados = set()):
        self.cerrados = cerrados #para no volver a expandir nodos ya visitados
        self.nodo = Nodo(estado.nodoInicio)
        self.frontera = set()
        #Para expandir nodos

    def Sucesor(self,problema, nodoActual):
        ret = set()
        while True:
            accionATomar = nodoActual.getNextSegment() #es uno de los segmentos de la interseccion en el nodo estado
            if (accionATomar == None):
                return ret
            sucesor = operaciones.getDestinationOf(accionATomar) #es la interseccion destino de accion
            tupla = (accionATomar, sucesor)
            ret.add(tupla)

    def testObjetivo(self,nodo,estado):
        return problema.getIntersectionId(nodo.estado) == estado.IdFinal

    def costeIndividual(self,origen,calle,destino):
        return accion.getDistanceOf(calle) / accion.getSpeedOf(calle)

    def listaSolucion(self,nodo):
        sol = []
        aux = nodo
        while (aux.padre):
            sol.append(aux.estado)
            aux = aux.padre
        sol.append(aux.estado)
        return sol

    def expandir(self,nodo,problema):
        sucesores = []
        for (accionTomada,resultado) in self.Sucesor(problema,nodo):
            if (not (problema.getIntersectionId(resultado) in self.cerrados)):
                s = Nodo(resultado, nodo, accionTomada)
                s.coste = nodo.coste + self.costeIndividual(nodo,accionTomada,s)
                s.profundidad = nodo.profundidad + 1
                sucesores.append(s)
        return sucesores

    def bus(self):
        self.frontera.add(self.nodo) 
        while(True):
            self.nodo = self.seleccionSiguienteNodo(self.frontera)
            #estado = Estado()
            self.cerrados.add(problema.getIntersectionId(self.nodo.estado))
            if (len(self.frontera) == 0):
                return Exception
            self.frontera.remove(self.nodo)
            if (self.testObjetivo(self.nodo,estado)):
                return self.listaSolucion(self.nodo)
            nose = self.expandir(self.nodo,problema)
            self.frontera = self.frontera.union(nose)

# Expandir -> Entra un nodo.Coge todos las intersecciones posibles y las mete a frontera. Id mas bajo primero
# Accion -> 
# Estado -> Quitar inicio y final y ponerlos en problema OTRA VEZ
# Estado -> dentro de nodo. Tiene solo los atributos de la interseccion
# Cerrados -> Identificador
# Frontera -> Lista
# Segmento -> Diccionario
# Heuristica -> en ClaseBúsqueda
# Estado -> tener basicamente todas las operaciones. Tendrá el nodo actual almacenado asi que no habra
# que pasarle la interseccion / seccion a cada metodo
# Heuristica -> Mediante una PriorityQueue(Id,Nodo)
# lt(a,b) -> a<b
# ll(a,b) -> a<=b
# eq(a,b) -> a==b
# ge(a,b) -> a>=b
# gt(a,b) -> a>b

