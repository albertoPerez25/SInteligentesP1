import json

#Abrimos el archivo json y lo guardamos en una variable
with open('/home/calberto/Documents/Uni/5toCuatri/SistemasInteligentes/Practicas/P1/pr1_SSII/problems/small/avenida_de_espana_250_0.json', 'r') as file:
    new_dictionary = json.load(file)

print (new_dictionary)
print("------------------------")
#El diccionario del json, en el apartado intersections tiene otro diccionario
print (new_dictionary["intersections"])
print("------------------------")
print (new_dictionary["segments"])


#intersections = {"identifier": ,"longitude": ,"latitude": }

#Hacemos el diccionario intersections que tiene el diccionario dentro de new_dictionary[intersections]
intersections = new_dictionary["intersections"]
segments = new_dictionary["segments"]

#Hacemos un objeto
class Estado: #En que interseccion estas son sus segmentos
    def __init__(self, id, interseccion):
        self.id = id
        self.interseccion = interseccion

    def __str__(self):
        return f"State(id={self.id}, intersection_id={self.interseccion})"

    def __repr__(self):
        return self.__str__()

    def get_interseccion(self):
        return self.interseccion

    def update_interseccion(self, new_interseccion_id):
        self.interseccion = new_interseccion_id
class Accion: #Irnos por un segmento (calle) u otra. Al elegir un segmento
    # actualizar Estado con el del campo "final" del segmento escogido

    def __init__(self, interseccion, calleElegida):
        self.Nodo = interseccion
        self.calleElegida = calleElegida

    def __str__(self):
        return f"At the intersection {self.interseccion}, choose {self.calleElegida}"

    def __repr__(self):
        return f"Action(intersection='{self.interseccion}', chosen_street='{self.calleElegida}')"
    def irCalle(self):
        return self.interseccion.get_neighbors()[0]
    
class Nodo: #representa (creo que todas) las intersecciones y sus segmentos asociados. 
    #Los segmentos se relacionan entre si y con las intersecciones 
    # mediante origin y destination, que contienen ids de intersecciones
    def __init__(self, id, latitude, longitude,speed, index = 0):
        self.id = id 
        self.latitude = latitude
        self.longitude = longitude
        self.speed = speed
        self.neighbors = []
        self.index = index

    def __str__(self):
        return f"Node(id={self.id}, latitude={self.latitude}, longitude={self.longitude})"

    def __repr__(self):
        return self.__str__()

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def remove_neighbor(self, neighbor):
        if neighbor in self.neighbors:
            self.neighbors.remove(neighbor)
            return True
        return False
    
    def next_neighbor(self):
        if self.index < len(self.neighbors):
            self.index=self.index+1
            return True
        return False
    
    def get_neighbors(self):
        return self.neighbors
    
    def get_currentNeighbor(self):
        return self.neighbors[self.index]

    def get_coordinates(self):
        return (self.latitude, self.longitude)

class Problema:
    def __init__(self,id,latitud,longitud):
        self.id = id
        self.latitud = latitud
        self.longitud = longitud


#Inicializamos el objeto
estado = Estado(3,4,5)
print(estado.id)
print(estado.latitud)
print(estado.longitud)
