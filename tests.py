import json
import time

#Abrimos el archivo json y lo guardamos en una variable
# with open('/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/problems/small/avenida_de_espana_250_0.json', 'r') as file:
    #new_dictionary = json.load(file)

#print (new_dictionary)
print("------------------------")
#El diccionario del json, en el apartado intersections tiene otro diccionario
#print (new_dictionary["intersections"])
print("------------------------")
#print (new_dictionary["segments"])


#intersections = {"identifier": ,"longitude": ,"latitude": }

#Hacemos el diccionario intersections que tiene el diccionario dentro de new_dictionary[intersections]
#intersections = new_dictionary["intersections"]
#segments = new_dictionary["segments"]

# Load JSON data
#with open('/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/problems/small/paseo_simon_abril_250_0.json', 'r') as file:
 #   data = json.load(file)
#with open('/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/Proyecto/recursos/problems/medium/calle_maria_marin_500_0.json', 'r') as file:
#    data = json.load(file)
with open('/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/Proyecto/recursos/problems/test/test.json', 'r') as file:
    data = json.load(file)

class Intersection:
    def __init__(self, id, latitude, longitude):
        self.identifier = id
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"Intersection(id={self.identifier}, latitude={self.latitude}, longitude={self.longitude})"

# Convert intersections
intersections = set()
for intersection in data['intersections']:
    identifier = intersection['identifier']
    print(intersection)
    intersections.add(Intersection(identifier, intersection['latitude'], intersection['longitude']))

class Segment:
    def __init__(self, origin, destination, distance, speed):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.speed = speed

segments = set()
for seg in data['segments']:
    print (seg)
    segments.add(Segment(seg['origin'], seg['destination'], seg['distance'], seg['speed']))




intersection_dic = {i.identifier: i for i in intersections}
segment_dic = {(s.origin, s.destination): s for s in segments}

#print(intersection_dic[1530850331])
#print(intersection_dic[1530850331].latitude)


######################################################################

#Hacemos un objeto
class EstadoAux: #En que interseccion estas con sus segmentos
    def __init__(self, intersection):
        self.identifier = intersection.identifier
        self.latitude = intersection.latitude
        self.longitude = intersection.longitude
    
    def getSegments(self):
        return NodoAux.getSegmentsOf(self.identifier)
    
    def getAllNearIntersections(self):
        return NodoAux.getAllNearIntersections(self.identifier)   
    
class Accion: #Irnos por un segmento (calle) u otra. Al elegir un segmento
    # actualizar Estado con el del campo "final" del segmento escogido

    def __init__(self, chosenSegment, intersection = 0):
        self.intersection = intersection
        self.chosenSegment = chosenSegment
    
    def getChosenIntersection(self):
        return self.chosenSegment.destination
    
    def setCurrent(self, intersection):
        return EstadoAux(intersection)
    
    
class NodoAux: #representa (creo que todas) las intersecciones y sus segmentos asociados. 
    #Los segmentos se relacionan entre si y con las intersecciones 
    # mediante origin y destination, que contienen ids de intersecciones
    def __init__(self, intersections_dir, segments):
        self.intersections = intersections_dir
        self.segments = segments

    def getSegmentsOf(self,id):
        aux = []
        for x in segments:
            if id==x.origin:
                aux.append(x)
        return aux

    def getIntersection(self, id):
        return self.intersections[id]
    
    def getIntersectionId(self, intersection):
        return intersection.identifier
    
    def getSpeedOf(self, segment):
        return segment.speed
    
    def getDistanceOf(self, segment):
        return segment.distance
    
    #Devuelve las intersecciones de todos los segmentos del id de la interseccion
    #que se le pase como parametro
    def getAllNearIntersections(self,id):
        listasospechosamentesospechosa = []
        test = self.getSegmentsOf(id)
        for i in range(0,len(test)):
            print(intersection_dic[test[i].destination])
            listasospechosamentesospechosa.append(intersection_dic[test[i].destination])
        return listasospechosamentesospechosa
    
    def getDestinationOf(self,segment):
        return intersection_dic[segment.destination]


class Problema:
    def __init__(self,solutionId):
        self.solutionId = solutionId
    
    def isSolution(self,intersection):
        return self.solutionId == intersection.identifier


## aLGORITMO Basico
def algoritmoSimple():
    inicial = 621983933
    final = 1322977378
    nodo = NodoAux(intersection_dic,segments)
    estado = EstadoAux(nodo.getIntersection(inicial))
    solucion = nodo.getIntersection(final)
    problema = Problema(final)
    solucion = []

    def funciondentrodefuncion():
        isSol = False
        it = 0
        while(not isSol):
            
            test = estado.getAllNearIntersections()

            for i in range(0,len(test)):
                print(test[i].identifier)

            isSol == problema.isSolution(test[it])
            Accion.setCurrent(test[it])

            it = it + 1


class Nodo:
    def __init__(self, interseccion, padre = None, accion = None, coste = 0, profundidad = 0):
        self.estado = interseccion
        self.padre = padre
        self.accion = accion
        self.coste = coste
        self.profundidad = profundidad

        self.calles = nodoaux.getSegmentsOf(nodoaux.getIntersectionId(self.estado))
        self.it = 0
        
    def __str__(self):
        return f"Nodo(estado={self.estado}, padre={self.padre}, accion={self.accion}, coste={self.coste}, profundidad={self.profundidad})"

    def getNextSegment(self,segments = []):
        if (len(segments) == 0):
            segments = self.calles
        if (self.it >= len(segments)):
            return None
        
        print(f"len: {len(segments)}")
        print(f"it: {self.it}")

        segment = segments[self.it]
        self.it = self.it + 1
        return segment


class Estado:
    def __init__(self,problema):
        self.nodo = problema


problema = {
    "inicial":data["initial"],
    "final":data["final"]
}
#print(problema["inicial"])
#print(problema["final"])
nodoaux = NodoAux(intersection_dic,segments)
estadoAux = EstadoAux(nodoaux.getIntersection(problema["inicial"]))
solucion = nodoaux.getIntersection(problema['final'])


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

frontera = []

def expandir(nodo,problema):
    sucesores = []
    for (accion,resultado) in Sucesor(problema,nodo):
        s = Nodo(resultado, nodo, accion)
        #s.padre = nodo
        #s.accion = accion
        s.coste = nodo.coste + costeIndividual(nodo,accion,s)
        s.profundidad = nodo.profundidad + 1
        sucesores.append(s)
    return sucesores

def busquedaArbol(problema,frontera):
    #print(nodoaux.getIntersection(problema["inicial"]))
    estado = Estado(nodoaux.getIntersection(problema["inicial"]))
    nodo = Nodo(estado.nodo)
    frontera.append(nodo)
    while(True):
        nodo = frontera[0]
        #print(frontera)
        if (len(frontera) == 0):
            return Exception
        print(f"nodo: {nodo} frontera: {frontera}")
        frontera.remove(nodo)
        if (testObjetivo(nodo,problema)):
            return listaSolucion(nodo)
        nose = expandir(nodo,problema)
        frontera.extend(nose)
        #time.sleep(0.5)

f = []
f.append(nodoaux.getIntersection(problema["inicial"]))

#print(estadoAux.identifier)
#print(nodoaux.getIntersection(problema["inicial"]))
fin = busquedaArbol(problema,[])
for i in fin:
    print(i)
print(f"FIN")
