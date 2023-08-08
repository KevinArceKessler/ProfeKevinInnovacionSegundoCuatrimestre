#Los diccionarios son una estructura de datos que nos permite almacenar
#información de manera organizada utilizando una clave para acceder a cada
#valor. Cada clave debe ser única y puede asociarse a cualquier valor, como números,
#cadenas de texto, listas, tuplas, funciones, etc. Los diccionarios se
#definen utilizando llaves ({}) y separando cada clave y su valor con dos puntos (:).

Personas= {34333726: "Kevin Kessler", 36555888: "Jorge Ruiz", 32555999: "Luisa Perez"}

#Se puede acceder mediante la clave al valor:
Personas['Kevin Kessler']

#Podemos obtener una lista con todas las claves del diccionario
Personas.keys()

#Podemos obtener una lista con todos los valores del diccionario
Personas.values()

#También podemos convertir el diccionario a una lista
Personas.items()


