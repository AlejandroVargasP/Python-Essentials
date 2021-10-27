# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 08:13:07 2021

@author: JUAN
"""

#OPERADORES LÓGICOS - BOOLEANOS

#Estructuras de flujo

"""
edad=int(input("Ingrese su edad como un número: "))

if edad>=18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
"""  
    
    
    
    
edad=int(input("Ingrese su edad como un número: "))

if edad<18:
    print("Usted es menor de edad")
elif edad>=18 and edad<45:
    print("Usted es un adulto joven") 
elif edad>=45 and edad<60:
    print("Usted es un adulto") 
else:
    print("Usted es un adulto mayor")
    
    
    


#Estructuras de Control

#While

"""
var1=1
while var1<10:
    print(var1)
    var1=var1+1
print("Fin del programa")
"""


num=int(input("Escriba un número positivo: "))
while num<0
    print("Número negativo, vuelva a ingresar")    
    num=int(input("Escriba un número positivo: "))
print("El número es correcto")




#Ejercicio

#Escribir un código que permita mostrar en pantalla lo que el usuario ingresa por teclado.
#Cuando el usuario ingresa la palabra salir (en may o min) se debe terminar la ejecución

#Crear un programa que se mantenga activo si se ingresa cualquier texto y se muestre en pantalla.
#Si ingresar la palabra Salir, el programa se detenga.

usr_ing=input("Ingrese una o mas palabras")
while usr_ing.lower() != "salir":
    print(usr_ing)
    usr_ing=input("Ingrese una o mas palabras")
print("Programa terminado")
    
    
usr_ing=input("Ingrese una o mas palabras")
while usr_ing.lower() == "salir":
    print(usr_ing)
    usr_ing=input("Ingrese una o mas palabras")
print("Programa terminado")


#Para que en una secuencia ciertos valores no aparezcan
x=1
while x<=10:
    if x==5:
        x+=1
        continue
    print(x)
    x+=1
    
    

for i in "Prueba":
    print("Número")
    print (i)
    
    
for ch in "Prueba":
    print("Repetición")
    print (ch)
    
    
#Range crea elementos iterativos
lst=range(4)
print(lst)
    
    
for ch in range(1,6):
    print("Repetición")
    print (ch)
    
    
#Ejercicio

#Escribir un programa que pregunte al usuario una frase y una letra, y muestre por pantalla
#el número de veces que aparece la letra en la frase.

frase_larga=input("Ingreso de la frase: ")
letra_bsq=input("Letra a contar: ")
cnt=0
for cntrl in frase_larga:
    if cntrl == letra_bsq:
        cnt+=1
print(cnt)



frase_larga=input("Ingreso de la frase: ")
letra_bsq=input("Letra a contar: ")
cnt=0
var=0
while var<len(frase_larga):
    
    if frase_larga[var]==letra_bsq
        cnt+=1
        
    var+=1
print(cnt)






    
    
    
    
    
    
    
    
    
    