import time
# tiempo en segundos desde el inicio del programa
start = time.perf_counter()
print(f"tiempo inicio: {start:.0f}") #quitamos los numeros despues de la coma

import random

p = open(r"F:\code\wordlee\prueba.txt", "r")
baseDeDatos = p.readlines()
p.close()
palabra = (random.choice(baseDeDatos))

palabra = palabra[:-1]

print("¡Bienvenido al juego WORDLE!")
print("Si lo resolves en 5 intentos o menos tu puntaje será de 100 puntos")
print("Si lo resolves en 10 intentos o menos tu puntaje será de 50 puntos")
print("Si lo resolves en más intentos tu puntaje será de 1 punto")

palabraIngresada = input("Ingrese una palabra de 5 letras: ")
cantIntentos = int(input("Ingrese la cantidad de intentos: "))

pMayu = palabraIngresada.upper()


intentos = 0
for i in range(cantIntentos+1):
    pMayu = palabraIngresada.upper()
    if palabra == pMayu:
        print("La palabra es correcta!")
        if intentos <= 5:
            print("Tu puntaje es de 100 puntos")
        elif intentos <= 10:
            print("Tu puntaje es de 50 puntos")
        else:
            print("Tu puntaje es de 1 punto porque tuviste muchos intentos")
        break
    for i in range(5):
        if palabra[i] == pMayu[i]:
            print("La letra ", palabra[i], " está en la posición correcta.")
        elif palabra[i] in pMayu:
            print("La letra ", palabra[i], " está en la palabra.")
    intentos += 1
    palabraIngresada = input("Ingrese una palabra de 5 letras: ")

# tiempo en segundos desde el inicio del programa
end = time.perf_counter()
print(f"tiempo fin: {end:.0f}")

# obtengo el tiempo que tardó entre end y start
print(f"transcurrió: {(end - start):.0f}")

