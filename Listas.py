#Una lista es un tipo de datos que se utiliza para almacenar una colección
#ordenada de elementos. Los elementos pueden ser de diferentes tipos de
#datos, como números, cadenas, booleanos, etc. Las listas se definen utilizando
#corchetes [], y los elementos se separan por comas , .

Numeros=[1,2,55,5.5,2589,102]

Personas=["Santiago", "Mónica", "Luis", "Emilse"]

Random=["Mario", 55, False, 5.9, '2023-08-05']

Vacio=[]

#Se puede acceder a los valores de las listas por medio de los índices:
print(Personas[1]) #Imprime el valor Mónica de la lista Personas.
print(Personas) #Imprime toda la lista.

#Se puede añadir elementos:
Personas.append("Kevin") #El append inserta al final de la lista
Personas.insert(2,"Hector") #El insert inserta en la posición que se le indica y luego el valor a insertar.

#Se puede eliminar elementos:
Personas.remove(3) #Elimina el elemento del índice 3.

#Se puede ordenar las listas, las ordena por orden ascendiente:
Personas.sort()
Personas.sort(reverse=True) #Ordena por orden descendiente.





