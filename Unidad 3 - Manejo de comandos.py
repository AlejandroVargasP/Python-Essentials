# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:27:22 2021

@author: JUAN
"""

#Secuencias de escape:

print("Mensaje de prueba uno\nSegunda línea del mensaje")

#\n salto línea
#\t sangría
#/*

#Mezclar distintos tips de valores (strings y números)

print("El siguiente es un número entero: ",50)

print("El siguiente es un número entero: ",50, "Número decimal: ", 78.92)

print("El siguiente es un número entero: ",50, "\nNúmero decimal: ", 78.92)    #muestra en una nueva línea

#Pruebas con Strings

var1="Texto1"
var2=643
var3=4.67
var4="Texto2"

print(var1,var2,var3,var4)

#Concatenación
#print(var1+var2+var3+var4)   #hay que cambiar de integer a strings

print(var1+str(var2)+str(var3)+var4)    #usar la función constructora str

print("Texto Prueba"+str(var2)+str(var3)+"98")

print(f"Variable1: {var1}\nVariable2: {var2}\nVariable3: {var3}\nVariable4: {var4}\n")  #cadenas tipo f

print(f"Variable1: {var1}\nVariable2: {var2/2}\nVariable3: {var3}\nVariable4: {var4}\n")  # se puede hacer operaciones dentro de la cadena

print("89+var2-var3")  #entre comillas solo los considera como strings, no como número

#Método format

print("Mi nombre es: {}, mi apellido es: {}, mi edad es: {}".format("Alejandro","Vargas",28))

#var5="Mi nombre es: {}, mi apellido es: {}, mi edad es: {}".format("Alejandro","Vargas",28)
#print(var5)     #otra forma de hacer pero crear muchas variables ocupa mucha memoria

#Puedo poner el órden de posición de los datos de manera interna en el paréntesis
print("Mi nombre es: {1}, mi apellido es: {1}, mi edad es: {1}".format("Alejandro","Vargas",28))

#creando variables localmente
print("Mi nombre es: {nombre}, mi apellido es: {apellido}, mi edad es: {edad}".format(nombre="Alejandro",apellido="Vargas",edad=28))

#No se puede hacer operaciones dentro de los corchetes del método format
#print("Mi nombre es: {nombre*2}, mi apellido es: {apellido}, mi edad es: {edad-10}".format(nombre="Alejandro",apellido="Vargas",edad=28))

#Se puede declarar sentencias en los argumentos del format
print("Mi nombre es: {nombre}, mi apellido es: {apellido}, mi edad es: {edad}".format(nombre="Alejandro"+"Prueba",apellido="Vargas",edad=28-10))


#













