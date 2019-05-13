#creamos un archivo nuevo
#guardamos en la carpeta del repositorio
#con la extension ".py"
#uso de nuemros aleatorios


#importamos la libreria randint
from random import randint
aleatorio=randint(0,20) #creamos una variable y generamos un numero aleatorio entre 0 y 20
print(aleatorio)#imprimimos el numero generado

#ejercicio
#escribir una funcion sorteo() que reciba una lista de participantes, y elegir a uno de los
#participantes aleatoriamente, y retornar esa persona elegida
#desafio: no volver a retornar una persona ya sorteada 

#importamos la funcion randint de libreria random
from random import randint
    def sorteo(lista):      #definimos una funcion
        cant=len(lista)-1   #utilizamos len() para saber la cantidad de personas que hay en la lista y guardamos en cant
        indice=randint(0,cant)  #generamos un indice aleatorio
        ganador=lista[indice]   #seleccinamos un elemento de la lista y guardamos en la variable a retornar "ganador"
        return ganador          #retornamos ganador

participantes=["Ale","Vero","Fede","Adolf"] #creamos la lista de los participantes
ganar=sorteo(participantes)                 #llamamos a la funcion y lo guardamos en una variable el resultado retornado por la funcion
print(ganar)                                #imprimimos "ganador"
