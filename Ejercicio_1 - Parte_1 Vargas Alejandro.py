# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 08:56:01 2021

@author: Alejandro Vargas
"""

#Realizado por: “Alejandro Vargas Pacha”

#Ejercicio_1 - Parte_1


print("Consultando los tipos de valores:")

#Para analizar el tipo de dato de las variables 1, 2, 3, 4; se utilizará el comando print(type(Var2))
      
Var1=875
print("El tipo de dato de 875 es: ")
print(type(Var1))


Var2=4.89
print("El tipo de dato de 4.89 es: ")
print(type(Var2))


Var3="Now is better than never."
print("El tipo de dato del texto: Now is better than never. es: ")
print(type(Var3))


Var4=1.32
print("El tipo de dato de 1.32 es: ")
print(type(Var4))


#Para responder si el tipo de dato de las variables 5, 6, 7 corresponde a un tipo específico, se utilizará la función lógica if-else

Var5=5+8j
print("¿El valor 5 + 8i corresponde a un valor entero? ")
if type(Var5)==int:
    print("Verdadero")
else:
    print("Falso")


Var6=8.2
print("¿El valor 8.2 corresponde a un valor entero? ")
if type(Var6)==int:
    print("Verdadero")
else:
    print("Falso")


Var7="Readability counts."
print("¿El texto: Readability counts. corresponde a un string?")
if type(Var7)==str:
    print("Verdadero")
else:
    print("Falso")

