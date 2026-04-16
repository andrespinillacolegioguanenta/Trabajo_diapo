# Programa del trabajo N°4

#libreria
import random

numeros = [random. randint(-100, 100) for _ in range(20)] # Genera una listade 20 números aleatorios entre -100 y 100 
print( "Números generados:", len(numeros))
print()
print("los numeros son: ", numeros)

positivos = [pos for pos in numeros if pos > 0]
print ()
print ("los numeros positivos son:", positivos)




