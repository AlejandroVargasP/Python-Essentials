# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:20:53 2021

@author: JUAN
"""

#EJERCICIO 1:

#Escribir un programa que pregunte al usuario los productos de una carrito de 
#compras, separados por comas, y muestre por pantalla cada uno de los productos 
#en una línea distinta

#1ra Solución limitar el número de prodcutos que ingresan
compras="manzanas, libros, chocolates"
c1=["manzanas","libros","chocolates"]

compras=input("INGRESAR CUATRO PRODUCTOS DEL CARRO SEPARADO POR COMAS: ")
z=compras.split(",")
print("Artículo 1: {}\nArtículo 2: {}\nArtículo 3: {}\nArtículo 4: {}\n".format(z[0],z[1],z[2],z[3]))


#2da Solución
compras=input("INGRESAR CUATRO PRODUCTOS DEL CARRO SEPARADO POR COMAS: ")
compras_p=compras.replace(",", "\n")
print(compras_p)
















