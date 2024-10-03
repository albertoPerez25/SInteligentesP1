import json

#Abrimos el archivo json y lo guardamos en una variable
with open('/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/problems/small/avenida_de_espana_250_0.json', 'r') as file:
    new_dictionary = json.load(file)

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
with open('/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/problems/small/avenida_de_espana_250_0.json', 'r') as file:
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
    intersections.add(Intersection(identifier, intersection['latitude'], intersection['longitude']))

class Segment:
    def __init__(self, origin, destination, distance, speed):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.speed = speed

segments = set()
for seg in data['segments']:
    segments.add(Segment(seg['origin'], seg['destination'], seg['distance'], seg['speed']))




intersection_dic = {i.identifier: i for i in intersections}
segment_dic = {(s.origin, s.destination): s for s in segments}

print(intersection_dic[1530850331])
print(intersection_dic[1530850331].latitude)


######################################################################

#Hacemos un objeto
class Estado: #En que interseccion estas con sus segmentos
    def __init__(self, intersection):
        self.identifier = intersection.identifier
        self.latitude = intersection.latitude
        self.longitude = intersection.longitude
    
    def getSegments(self):
        return Nodo.getSegmentsOf(self.identifier)
    
    def setCurrent(self, intersection):
        self.__init__(intersection)
   
class Accion: #Irnos por un segmento (calle) u otra. Al elegir un segmento
    # actualizar Estado con el del campo "final" del segmento escogido

    def __init__(self, chosenSegment, intersection = 0):
        self.intersection = intersection
        self.chosenSegment = chosenSegment
    
    def getchosenIntersection(self):
        return self.chosenSegment.destination
    
class Nodo: #representa (creo que todas) las intersecciones y sus segmentos asociados. 
    #Los segmentos se relacionan entre si y con las intersecciones 
    # mediante origin y destination, que contienen ids de intersecciones
    def __init__(self, intersections, segments):
        self.intersections = intersections
        self.segments = segments

    def getSegmentsOf(self,id):
        return self.segments[id]
    
    def getIntersection(self, id):
        return self.intersections[id]

class Problema:
    def __init__(self,intersection,solutionId):
        self.intersection = intersection
        self.solutionId = solutionId
    
    def isSolution(self):
        return self.solutionId == self.intersection.identifier
    
