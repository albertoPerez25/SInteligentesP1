from clasesBasicas import problema,Nodo,Estado

class Busqueda:
    def __init__(self,cerrados = set()):
        self.cerrados = cerrados #para no volver a expandir nodos ya visitados
        self.nodo = Nodo(problema.nodoInicio)
        self.frontera = []
        #Para expandir nodos

    def testObjetivo(self,nodo,estado):
        return estado.__eq__(problema.nodoFinal)

    def costeIndividual(self,origen,calle,destino):
        return origen.getDistanceOf(calle) / origen.getSpeedOf(calle)

    def listaSolucion(self,nodo):
        sol = []
        aux = nodo
        while (aux.padre):
            sol.append(aux.estado)
            aux = aux.padre
        sol.append(aux.estado)
        return sol

    def sucesor(self,problema, nodoActual):
        ret = set()
        while True:
            accionATomar = nodoActual.getNextSegment() #es uno de los segmentos de la interseccion en el nodo estado
            if (accionATomar == None):
                return ret
            sucesorId = nodoActual.getIntersectionId(nodoActual.getDestinationOf(accionATomar)) #es la interseccion destino de accion
            tupla = (accionATomar, sucesorId)
            ret.add(tupla)

    def expandir(self,nodo,problema):
        def orden(n):
            return nodo.getIntersectionId(n.estado)
        
        sucesores = []
        for (accionTomada,resultadoId) in self.sucesor(problema,nodo):
            if (not resultadoId in self.cerrados):
                s = Nodo(problema.getIntersection(resultadoId), nodo, accionTomada)
                s.coste = nodo.coste + self.costeIndividual(nodo,accionTomada,s)
                s.profundidad = nodo.profundidad + 1
                sucesores.append(s)
        sucesores.sort(key = orden)
        return sucesores

    def bus(self):
        self.frontera.append(self.nodo) 
        while(True):
            if (len(self.frontera) == 0):
                return Exception
            self.nodo = self.seleccionSiguienteNodo(self.frontera)
            #estado = Estado()
            self.cerrados.add(self.nodo.getIntersectionId(self.nodo.estado))
            self.frontera.remove(self.nodo)
            if (self.testObjetivo(self.nodo,self.nodo.estado)):
                return self.listaSolucion(self.nodo)
            nose = self.expandir(self.nodo,problema)
            self.frontera.extend(nose)

#TAREAS A HACER
# 1.!HECHO Expandir -> Entra un nodo.Coge todos las intersecciones posibles y las mete a frontera. Id mas bajo primero
# 2.!HECHO Frontera -> Lista
# 3.!HECHO Accion -> Tiene un solo segmento guardado. El de la clase nodo. Dentro de nodo.
# 4.!HECHO Estado -> Quitar inicio y final y ponerlos en problema OTRA VEZ
# 5.!HECHO Estado -> dentro de nodo. Tiene solo los atributos de la interseccion
# 6.!HECHO Nodo -> tener basicamente todas las operaciones. Tendrá el nodo actual almacenado asi que no habra
#                  que pasarle la interseccion / seccion a cada metodo
# 7.!HECHO ClaseBusqueda -> Cambiar llamadas a metodos por las nuevas
# 8.!HECHO Actualizar metodos de algoritmos para llamar a los nuevos metodos
# 9.Segmento -> Diccionario
# 10.Heuristica -> en ClaseBúsqueda
# 11.Heuristica -> Mediante una PriorityQueue(Id,Nodo)

#OTRAS NOTAS
# Cerrados -> Identificador

# lt(a,b) -> a<b
# ll(a,b) -> a<=b
# eq(a,b) -> a==b
# ge(a,b) -> a>=b
# gt(a,b) -> a>b

