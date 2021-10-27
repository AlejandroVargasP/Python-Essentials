# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:37:42 2021

@author: JUAN
"""

#Unidad 5 - Módulos, paquetes y excepciones

#Módulos


def construccion(nombre,apellido):
    return (f"Nombre:{nombre}, Apellido:{apellido}")

def adicion(num1, num2, num3):
    return num1+num2+num3

def pantalla():
    print("FUNCIÓN VACIA")
    return


import modulo_1  #Para llamar funciones creadas en otros archivos que se podr{ia llamar por ej "modulo_1"}

modulo_1.pantalla()            #Para llamar específicamente a una función
modulo_1.adicion(5,2,3)
modulo_1.construccion()


from modulo_1 import pantalla
pantalla()

from modulo_1 import pantalla,adicion,construccion

from modulo_1 import *

adicion(5,2,3)
construccion("Name", "LastName")


#Si tenemos cada función en archivos diferentes, por ej: modulo_1, modulo_2, modulo_3 

































