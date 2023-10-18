import math
import random

def ingresar_nombre_y_edad():
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")

def calcular_area_circulo(radio):
    return math.pi * radio**2

def generar_lista_numeros_aleatorios(cantidad):
    return [random.randint(1, 100) for _ in range(cantidad)]

def es_par_o_impar(numero):
    if numero % 2 == 0:
        return f"{numero} es un número par."
    else:
        return f"{numero} es un número impar."

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def calcular_suma_lista(numeros):
    return sum(numeros)

def encontrar_maximo_minimo(lista):
    maximo = max(lista)
    minimo = min(lista)
    return f"El número más grande en la lista es: {maximo}\nEl número más pequeño en la lista es: {minimo}"

def invertir_lista(lista):
    return lista[::-1]

def generar_matriz(filas, columnas):
    matriz = [[0] * columnas for _ in range(filas)]
    return matriz

def calcular_factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

def generar_lista_numeros_pares(inicio, fin):
    return [num for num in range(inicio, fin + 1) if num % 2 == 0]

def imprimir_numeros_del_1_al_10():
    for num in range(1, 11):
        print(num)

def operaciones_aritmeticas(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    return f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}"

def calcular_media_aritmetica(lista):
    if not lista:
        return 0
    suma = sum(lista)
    return suma / len(lista)