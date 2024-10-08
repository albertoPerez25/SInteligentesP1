#GRUPO 9
#ALBERTO PEREZ ALVAREZ
#MARCOS LOPEZ GOMEZ

import json
RUTAJSON = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/Proyecto/recursos/problems/test/test.json'
RUTAJSON = '/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/Proyecto/recursos/problems/medium/calle_maria_marin_500_0.json'


with open(RUTAJSON, 'r') as file:
    data = json.load(file)

#Creamos clases para tener objetos que contengan las intersecciones y segmentos del JSON
class Intersection:
    def __init__(self, id, latitude, longitude):
        self.identifier = id
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"Interseccion: (id={self.identifier}, latitud={self.latitude}, longitud={self.longitude})"

class Segment:
    def __init__(self, origin, destination, distance, speed):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.speed = speed

#Pasamos las intersecciones del JSON a a un conjunto de objetos
intersections = set()
for intersection in data['intersections']:
    identifier = intersection['identifier']
    intersections.add(Intersection(identifier, intersection['latitude'], intersection['longitude']))

segments = set()
for seg in data['segments']:
    segments.add(Segment(seg['origin'], seg['destination'], seg['distance'], seg['speed']))

#convertimos el conjunto de intersections a un diccionario
intersection_dic = {i.identifier: i for i in intersections}
#Segmentos no tiene sentido pues no tiene un id

#Cargamos en el diccionario problema los nodos iniciales y finales del JSON
problema = {
    "inicial":data["initial"],
    "final":data["final"]
}

#Clase con funciones para no tener que operar con los datos directamente
class NodoAux: 
    #representa las intersecciones y sus segmentos asociados. 
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

  
nodoaux = NodoAux(intersection_dic,segments)
solucion = nodoaux.getIntersection(problema['final'])

