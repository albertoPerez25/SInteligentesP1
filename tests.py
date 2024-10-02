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
class Estado: #En que interseccion estas
    def __init__(self, id, id_interseccion):
        self.id = id
        self.id_interseccion = id_interseccion

    def __str__(self):
        return f"State(id={self.id}, intersection_id={self.id_interseccion})"

    def __repr__(self):
        return self.__str__()

    def get_interseccion(self):
        return self.id_interseccion

    def update_interseccion(self, new_interseccion_id):
        self.id_interseccion = new_interseccion_id
class Accion: #lo que puedes hacer en una interseccion
    def __init__(self, interseccion, calleElegida):
        self.Nodo = interseccion
        self.calleElegida = calleElegida

    def __str__(self):
        return f"At the intersection {self.interseccion}, choose {self.calleElegida}"

    def __repr__(self):
        return f"Action(intersection='{self.interseccion}', chosen_street='{self.calleElegida}')"
    def irCalle(self):
        return self.interseccion.get_neighbors()[0]
    
class Nodo: #representa una interseccion
    def __init__(self, id, latitude, longitude):
        self.id = id 
        self.latitude = latitude
        self.longitude = longitude
        self.neighbors = []

    def __str__(self):
        return f"Node(id={self.id}, latitude={self.latitude}, longitude={self.longitude})"

    def __repr__(self):
        return self.__str__()

    def remove_neighbor(self, neighbor):
        if neighbor in self.neighbors:
            self.neighbors.remove(neighbor)
            return True
        return False

    def get_neighbors(self):
        return self.neighbors

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
