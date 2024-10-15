#GRUPO 9 - 3ºB esiiab
#ALBERTO PEREZ ALVAREZ
#MARCOS LOPEZ GOMEZ

import json
from math import sqrt

#RUTAJSON = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/Proyecto/recursos/problems/test/test.json'
#RUTAJSON = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/Proyecto/recursos/problems/medium/calle_maria_marin_500_0.json'
#RUTAJSON = '/home/marcos/Documentos/3_Uni/Sistemas_Inteligentes/Programas_python/SInteligentesP1/recursos/problems/medium/calle_maria_marin_500_0.json'
#RUTAJSON = '/home/marcos/Documentos/3_Uni/Sistemas_Inteligentes/Programas_python/SInteligentesP1/recursos/problems/test/test.json'

with open(RUTAJSON, 'r') as file:
    data = json.load(file)

class Problema:   
    #Creamos clases para tener objetos que contengan las intersecciones
    class Intersection:
            def __init__(self, id, latitude, longitude):
                self.identifier = id
                self.latitude = latitude
                self.longitude = longitude

            def __str__(self):
                return f"Interseccion: (id={self.identifier}, latitud={self.latitude}, longitud={self.longitude})"

    #Constructor de Problema
    def __init__(self,data):
        self.data=data
 
        #Pasamos las intersecciones del JSON a a un conjunto de objetos
        #self.intersections = set()
        #for intersection in self.data['intersections']:
        #    self.intersections.add(self.Intersection(intersection['identifier'], intersection['latitude'], intersection['longitude']))

        #convertimos el conjunto de intersections a un diccionario
        #self.intersection_dic = {i.identifier: i for i in self.intersections}

        ####PRUEBAS{
        #print(self.intersection_dic)
        #print()

        #self.intersection_dic.clear()

        #Pasamos las intersecciones del JSON a un nuevo diccionario
        self.intersection_dic = {}
        for intersection in self.data['intersections']:
            self.intersection_dic.update({intersection['identifier']:self.Intersection(intersection['identifier'], intersection['latitude'], intersection['longitude'])})
        
        #print(self.intersection_dic)
        ####}

        #Cargamos en el diccionario extremo los nodos iniciales y finales del JSON
        self.extremo = {
            "inicial":data["initial"],
            "final":data["final"]
        }
    #Agregar metodos de nodoAux que usen intersection_dic
    def getIntersection(self, id):
        return self.intersection_dic[id]

    def getIntersectionId(self, intersection):
        return intersection.identifier

class Accion:
    class Segment:
        def __init__(self, origin, destination, distance, speed):
            self.origin = origin
            self.destination = destination
            self.distance = distance
            self.speed = speed
            

    def __init__(self,data):
        self.data = data
        self.maxSpeed = 0

        self.segments = set()
        for seg in self.data['segments']:
            if (seg['speed'] > self.maxSpeed):
                self.maxSpeed = seg['speed']
            self.segments.add(self.Segment(seg['origin'], seg['destination'], seg['distance'], seg['speed']))
        
        #Segmentos no tiene sentido pasarlo a diccionario pues no tiene un campo id único
    #Agregar metodos de nodoAux que usen segments
    def getSegmentsOf(self,id):
        aux = []
        for x in self.segments:
            if id==x.origin:
                aux.append(x)
        return aux
    
    def getSpeedOf(self, segment):
        return segment.speed
    
    def getDistanceOf(self, segment):
        return segment.distance

problema = Problema(data)
accion = Accion(data)

#Habra metodos de nodoAux que quizas usen tanto segments como intersections_dic, esos habra que meterlos en otra clase especial para ellos
class Operaciones:
    def __init__(self, intersections_dir, segments):
        self.intersections_dic = intersections_dir
        self.segments = segments
    
    #Devuelve las intersecciones de todos los segmentos del id de la interseccion
    #que se le pase como parametro
    def getAllNearIntersections(self,id):
        listasospechosamentesospechosa = []
        test = accion.getSegmentsOf(id)
        for i in range(0,len(test)):
            print(self.intersections_dic[test[i].destination])
            listasospechosamentesospechosa.append(self.intersection_dic[test[i].destination])
        return listasospechosamentesospechosa
    
    def getDestinationOf(self,segment):
        return self.intersections_dic[segment.destination]


operaciones = Operaciones(problema.intersection_dic, accion.segments)
class Nodo:
    def __init__(self, interseccion, padre = None, accionTomada = None, coste = 0, profundidad = 0):
        self.estado = interseccion
        self.padre = padre
        self.accion = accionTomada
        self.coste = coste
        self.profundidad = profundidad

        #Lista de calles de la interseccion
        self.calles = accion.getSegmentsOf(problema.getIntersectionId(self.estado))
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
        self.nodoInicio = problema.getIntersection(problema.extremo["inicial"])
        self.nodoFinal = problema.getIntersection(problema.extremo["final"]) 
        self.IdInicio = problema.extremo["inicial"]
        self.IdFinal = problema.extremo["final"]

    def getDistanceToFinal(self, nodo):
        #Dos heuristicas:
        #Restar long y lat iniciales menos finales
        Ha = abs(nodo.estado.latitude - self.nodoFinal.latitude) + abs(nodo.estado.longitude - self.nodoFinal.longitude)
        #Pitágoras
        Hb = sqrt((nodo.estado.latitude - self.nodoFinal.latitude)**2 + (nodo.estado.longitude - self.nodoFinal.longitude)**2)
        #Ha da distancias mayores que Hb.
        #print("Ha: ",Ha)
        #print("Hb: ",Hb)
        return Ha
    
estado = Estado(problema)

