import json

with open('./recursos/problems/small/avenida_de_espana_250_0.json', 'r') as file:
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

class Estado:
    def __init__(self,id,latitud,longitud):
        self.id = id
        self.latitud = latitud
        self.longitud = longitud

estado = Estado(3,4,5)
print(estado.id)
print(estado.latitud)
print(estado.longitud)
