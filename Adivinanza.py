#juegpo de adivinar el numero, todos juntos, adivinar un numero generado aleatoriamente,
#ir introduciendo por teclado el dato a adivinar

from random import randint
generado=randint(0,10)#generamos el numero aleatorio
print(generado)                 #trampa
condicion=True
intento=10
while condicion:
    if intento>0:
        numero=input("Dame un numero del 0 al 10: ")
        contador=contador-1     #intento +=1
        if generado==int(numero):
            print("ganaste una anvorgesa que Lore paga")
            condicion=False
        else:
            print("El perdedor compra pizza a Lore")
            print("Te quedan",intento,"intentos")
    else:
        condicion=False
        print("Perdiste")