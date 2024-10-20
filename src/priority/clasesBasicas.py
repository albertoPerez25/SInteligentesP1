#GRUPO 9 - 3ºB esiiab
#ALBERTO PEREZ ALVAREZ
#MARCOS LOPEZ GOMEZ

import json
from math import sqrt

#RUTAJSON = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/Proyecto/recursos/problems/large/calle_f_albacete_5000_4.json'
RUTAJSON = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/Proyecto/recursos/problems/huge/calle_agustina_aroca_albacete_5000_0.json'
#RUTAJSON = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/Proyecto/recursos/problems/test/test.json'
#RUTAJSON = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/Proyecto/recursos/problems/medium/calle_maria_marin_500_0.json'
#RUTAJSON = '/home/marcos/Documentos/3_Uni/Sistemas_Inteligentes/Programas_python/SInteligentesP1/recursos/problems/medium/calle_maria_marin_500_0.json'
#RUTAJSON = '/home/marcos/Documentos/3_Uni/Sistemas_Inteligentes/Programas_python/SInteligentesP1/recursos/problems/test/test.json'

with open(RUTAJSON, 'r') as file:
    data = json.load(file)

#Interseccion:
class Estado:
    def __init__(self, id, latitude, longitude):
        self.identifier = id
        self.latitude = latitude
        self.longitude = longitude
    def __str__(self):
        return f"Interseccion: (id={self.identifier}, latitud={self.latitude}, longitud={self.longitude})"
    def __eq__(self, otro):
        if not isinstance(otro, Estado):
            return False
        else:
            return self.identifier == otro.identifier
    def __lt__(self, otro):
        return self.identifier < otro.identifier

#Segmento:    
class Accion:
    def __init__(self, origin, destination, distance, speed):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.speed = speed

class Problema:   
    #Creamos clases para tener objetos que contengan las intersecciones
        #Ahora estas clases son Estado(para intersecciones) y Accion(para segmentos/calles)

    #Constructor de Problema
    def __init__(self,data):
        self.data=data
        #Pasamos las intersecciones del JSON a un nuevo diccionario
        self.intersection_dic = {}
        for intersection in self.data['intersections']:
            self.intersection_dic.update({intersection['identifier']:Estado(intersection['identifier'], intersection['latitude'], intersection['longitude'])})

        #Cargamos en el diccionario extremo los nodos iniciales y finales del JSON
        self.extremo = {
            "idInicial":data["initial"],
            "idFinal":data["final"]
        }
        self.nodoInicio = self.getIntersection(self.extremo["idInicial"])
        self.nodoFinal = self.getIntersection(self.extremo["idFinal"]) 

        self.data = data
        self.maxSpeed = 0

        self.segments = set()
        for seg in self.data['segments']:
            if (seg['speed'] > self.maxSpeed):
                self.maxSpeed = seg['speed']
            self.segments.add(Accion(seg['origin'], seg['destination'], seg['distance'], seg['speed']))

    #Agregar metodos de nodoAux que usen intersection_dic
    def getIntersection(self, id):
        return self.intersection_dic[id]

    def getDestinationOf(self,segment):
        return self.intersection_dic[segment.destination]

    #Agregar metodos de nodoAux que usen segments
    def getSegmentsOf(self,id):
        aux = []
        for x in self.segments:
            if id==x.origin:
                aux.append(x)
        return aux

problema = Problema(data)

class Nodo:
    def __init__(self, interseccion, padre = None, accionTomada = Accion(1,1,1,1), coste = 0, profundidad = 0):
        self.estado = interseccion
        self.padre = padre
        self.accion = accionTomada
        self.coste = coste
        self.profundidad = profundidad
        #Estado(interseccion.identifier, interseccion.latitude, interseccion.longitude)
        #Accion(accionTomada.origin, accionTomada.destination, accionTomada.distance, accionTomada.speed)
        #Lista de calles de la interseccion
        self.calles = self.getSegmentsOf(self.getIntersectionId(self.estado))
        self.it = 0 #Iterador para self.calles
        
    def __str__(self):
        return f"Nodo(estado={self.estado}, padre={self.padre}, accion={self.accion}, coste={self.coste}, profundidad={self.profundidad})"

    def __eq__(self,otro):
        if not isinstance(otro, Nodo):
            return False
        return self.estado.__eq__(otro.estado) and self.accion.__eq__(otro.accion) and self.padre.__eq__(otro.padre)
    def __lt__(self,otro):
        return self.estado.__lt__(otro.estado)
    #METODOS:

    #Devuelve la siguiente calle de la interseccion
    def getNextSegment(self,segments = []):
        if (len(segments) == 0):
            segments = self.calles
        if (self.it >= len(segments)):
            return None
        segment = segments[self.it]
        self.it = self.it + 1
        return segment
    
    #Agregar metodos de nodoAux que usen intersection_dic
    def getIntersectionId(self, intersection = None):
        if(intersection == None):
            return self.estado.identifier
        return intersection.identifier
    
    def getLatitude(self, intersection = None): #NOUSADO
        if(intersection == None):
            return self.estado.latitude
        return intersection.latitude
    
    def getLongitude(self, intersection = None): #NOUSADO
        if(intersection == None):
            return self.estado.longitude
        return intersection.longitude
    
    #Agregar metodos de nodoAux que usen segments
    def getSegmentsOf(self,id = None):
        if(id==None):
            return problema.getSegmentsOf(self.estado.identifier)
        return problema.getSegmentsOf(id)
    
    def getSpeedOf(self, segment = None):
        if(segment == None):
            return self.accion.speed
        return segment.speed
    
    def getDistanceOf(self, segment = None):
        if(segment == None):
            return self.accion.distance
        return segment.distance


    #Habra metodos de nodoAux que quizas usen tanto segments como intersections_dic, esos habra que meterlos en otra clase especial para ellos
        #Devuelve las intersecciones de todos los segmentos del id de la interseccion
        #que se le pase como parametro
    def getAllNearIntersections(self,id):#NOUSADO
        conjuntoconunnombreinnecesariamentelargo = set()
        test = self.getSegmentsOf(id)
        for i in range(0,len(test)):
            print(self.intersections_dic[test[i].destination])
            conjuntoconunnombreinnecesariamentelargo.add(self.intersection_dic[test[i].destination])
        return conjuntoconunnombreinnecesariamentelargo
    
    def getDestinationOf(self,segment = None):
        if segment == None:
            return problema.getDestinationOf(self.accion)
        return problema.getDestinationOf(segment)
    
    def getDistanceToFinal(self, nodo = None):
        if (nodo == None) :
            nodo = self
        #Dos heuristicas:
        #Restar long y lat iniciales menos finales
        Ha = abs(nodo.estado.latitude - problema.nodoFinal.latitude) + abs(nodo.estado.longitude - problema.nodoFinal.longitude)
        #Pitágoras
        Hb = sqrt((nodo.estado.latitude - problema.nodoFinal.latitude)**2 + (nodo.estado.longitude - problema.nodoFinal.longitude)**2)
        #Ha da distancias mayores que Hb.
        #print("Ha: ",Ha)
        #print("Hb: ",Hb)
        return Hb


        

