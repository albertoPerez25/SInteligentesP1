from clasesBasicas import problema,Nodo,Estado
import heapq,time


class Busqueda:
    def __init__(self,cerrados = set()):
        self.tInicio = 0
        self.tFinal = 0
        self.cerrados = cerrados #para no volver a expandir nodos ya visitados
        self.nodo = Nodo(problema.nodoInicio)
        self.frontera = []
        #Para expandir nodos
        #estadisticas:
        self.nExpandidos = 0
        self.nProfundidad = 0
        self.nCosteTotal = 0 #nodo.coste es acumulativo
        self.nExplorados = 0
        #self.nGenerados = 0
        
    def merge_priority_queues(self,pq1,pq2):
        merged_pq = []

        while pq1:
            heapq.heappush(merged_pq, heapq.heappop(pq1))
        while pq2:
            heapq.heappush(merged_pq, heapq.heappop(pq2))

        return merged_pq

    def testObjetivo(self,nodo,estado):
        return estado.__eq__(problema.nodoFinal)

    def costeIndividual(self,origen,calle,destino):
        return origen.getDistanceOf(calle) / origen.getSpeedOf(calle)

    def listaSolucion(self,nodo):
        sol = []
        solId = []
        aux = nodo
        self.nCosteTotal = aux.coste
        while (aux.padre):
            sol.append(aux.estado)
            solId.append(aux.getIntersectionId())
            aux = aux.padre
        sol.append(aux.estado)
        solId.append(aux.getIntersectionId())
        solId.reverse()
        print(solId)
        print("Expandidos: ",self.nExpandidos)
        print("Explorados: ",self.nExplorados)
        print("Profundidad: ",self.nProfundidad)
        print("Coste Total: ",self.nCosteTotal)
        print("Tiempo de ejecución algoritmo: ",(self.tFinal-self.tInicio) * 10**3, "ms")
        return sol

    def sucesor(self,problema, nodoActual):
        ret = set()
        accionATomar = nodoActual.getNextSegment() #es uno de los segmentos de la interseccion en el nodo estado
        while accionATomar != None:  
            sucesorId = nodoActual.getIntersectionId(nodoActual.getDestinationOf(accionATomar)) #es la interseccion destino de accion
            self.nExplorados = self.nExplorados + 1
            if (not sucesorId in self.cerrados):
                tupla = (accionATomar, sucesorId)
                ret.add(tupla)
            accionATomar = nodoActual.getNextSegment()
        return ret

    def expandir(self,nodo,problema):
        sucesores = []
        for (accionTomada,resultadoId) in self.sucesor(problema,nodo):
            s = Nodo(problema.getIntersection(resultadoId), nodo, accionTomada)
            s.coste = nodo.coste + self.costeIndividual(nodo,accionTomada,s)
            s.profundidad = nodo.profundidad + 1
            if s.profundidad > self.nProfundidad:
                self.nProfundidad = s.profundidad
            sucesores = self.añadir(s,sucesores)
            self.cerrados.add(s.getIntersectionId(s.estado))
        return sucesores

    def bus(self):
        self.tInicio = time.time()
        self.frontera = self.añadir(self.nodo)
        self.nExplorados = self.nExplorados + 1
        self.cerrados.add(self.nodo.getIntersectionId(self.nodo.estado))
        while(len(self.frontera) != 0):
            self.nodo = heapq.heappop(self.frontera)[1]
            if (self.testObjetivo(self.nodo,self.nodo.estado)):
                self.tFinal = time.time()
                return self.listaSolucion(self.nodo)
            nose = self.expandir(self.nodo,problema)
            self.nExpandidos = self.nExpandidos + 1
            self.frontera = self.merge_priority_queues(self.frontera, nose)
        raise Exception("Frontera vacia")
    


    

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
