#GRUPO 9
#ALBERTO PEREZ ALVAREZ
#MARCOS LOPEZ GOMEZ

import json

RUTAJSON = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/Proyecto/recursos/problems/test/test.json'
#RUTAJSON = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/Proyecto/recursos/problems/medium/calle_maria_marin_500_0.json'
#RUTAJSON = '/home/marcos/Documentos/3_Uni/Sistemas_Inteligentes/Programas_python/SInteligentesP1/recursos/problems/medium/calle_maria_marin_500_0.json'

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
        self.intersections = set()
        for intersection in self.data['intersections']:
            self.intersections.add(self.Intersection(intersection['identifier'], intersection['latitude'], intersection['longitude']))

        #convertimos el conjunto de intersections a un diccionario
        self.intersection_dic = {i.identifier: i for i in self.intersections}

        #Cargamos en el diccionario extremo los nodos iniciales y finales del JSON
        self.extremo = {
            "inicial":data["initial"],
            "final":data["final"]
        }
        #Agregar metodos de nodoAux que usen intersection_dic
        def getIntersection(self, id):
            return self.intersections_dic[id]
    
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

        self.segments = set()
        for seg in self.data['segments']:
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
    


#Habra metodos de nodoAux que quizas usen tanto segments como intersections_dic, esos habra que meterlos en otra clase especial para ellos
class Operaciones:
    def __init__(self, intersections_dir, segments):
        self.intersections_dic = intersections_dir
        self.segments = segments
    
    #Devuelve las intersecciones de todos los segmentos del id de la interseccion
    #que se le pase como parametro
    def getAllNearIntersections(self,id):
        listasospechosamentesospechosa = []
        test = self.getSegmentsOf(id)
        for i in range(0,len(test)):
            print(self.intersections_dic[test[i].destination])
            listasospechosamentesospechosa.append(self.intersection_dic[test[i].destination])
        return listasospechosamentesospechosa
    
    def getDestinationOf(self,segment):
        return self.intersection_dic[segment.destination]

#Pruebas
problema = Problema(data)
accion = Accion(data)
Operaciones = Operaciones(problema.intersection_dic, accion.segments)
print(f"{problema.intersection_dic} {problema.extremo["inicial"]} {problema.extremo["final"]}")