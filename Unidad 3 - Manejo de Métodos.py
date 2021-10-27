# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:18:34 2021

@author: JUAN
"""
#TARTAMIENTO DE STRINGS

#Función len permite contar los elemntos del arreglo

var_prueba="MENSAJE DE TRABAJO PARA PRUEBAS"
tamaño_arr=len(var_prueba)
print(tamaño_arr)


#muestra el caracter específico de esa posición, contando desde 0
var_prueba="MENSAJE DE TRABAJO PARA PRUEBAS"
print(var_prueba[0])

#asignación mejorada
var1=90
print(var1)
var1=var1+89
print(var1)

#Actualizar el valor de la variable, el objeto original no muta
var_prueba="MENSAJE DE TRABAJO PARA PRUEBAS"
print(var_prueba)
var_prueba=var_prueba+"Texto adicional"
print(var_prueba)

#Cortar el mensaje desde hasta
var_prueba="MENSAJE DE TRABAJO PARA PRUEBAS"
print(var_prueba[0:7])

var_prueba="MENSAJE DE TRABAJO PARA PRUEBAS"
print(var_prueba[7:])

#Para cortar desde el final
var_prueba="MENSAJE DE TRABAJO PARA PRUEBAS"
print(var_prueba[-8:-1])
print(var_prueba[-8])


#Método upper, pone todo en mayúsculas
var_prueba="MENSAJE DE TRABAJO PARA PRUEBAS"
print(var_prueba)

print(var_prueba.upper())    #mayúsculas
print(var_prueba.lower())    #minúsculas
print(var_prueba.title())    #como título
print(var_prueba.lstrip())   #elimina espacios

print(var_prueba.replace("E", "100"))

print(var_prueba.split())    #separa elementos

correo_prueba="mavp@gmail.com"
print(correo_prueba.split("@")) 















