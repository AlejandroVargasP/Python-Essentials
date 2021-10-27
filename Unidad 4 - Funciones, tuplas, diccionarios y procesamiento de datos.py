# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 08:20:53 2021

@author: JUAN
"""

#Unidad 4 - Funciones, tuplas, diccionarios y procesamiento de datos

#Listas

lst1=[12, 3.4, 4+9j, "Texto"]
print(lst1)
type(lst1)

lst2=list("Texto")
print(lst2)

str1="Texto Prueba"
lst3=list(str1)
print(lst3)

lst1.append("TEXTO2")
print(lst1)

lst4=list()
lst5=list()
print(lst4)
print(lst5)

lst4.append(8)
lst5.append(3+8j)
print(lst4)
print(lst5)


lst1.extend(4,12,89,"Text4")
print(lst1)

lst2.insert(0, "PRUEBA")
print(lst2)

lst2.insert(3, 67.86)
print(lst2)

del lst2[0]
print(lst2)

lst6=[5,3,4,"T","y",67,"S1","T",8,"T"]
lst6.remove("T")                            #Elimina uno por uno las coincidencias
print(lst6)

lst6.reverse()                              #Cambia el orden
print(lst6)

lst3.sort()
print(lst3)

lst3.sort(reverse=True)
print(lst3)

lst7=[7,9,12,45,21,60,45,21]
lst7.sort()
print(lst7)

#Operaciones inmutables

str1="Texto Prueba"
lst3=list(str1)
print(lst3)

sorted(lst3)

lst10=sorted(lst3)
print(lst10)

lst11=["CASA","manzana","Tomate","VioLeTa"]
sorted(lst11)
print(lst11)

lst11*5

min(lst7)
max(lst7)
lst7.index(9)
lst7.index(45)

lst1.index("manzana")

lst7.count(45)
lst7.count(60)

sum(lst7)

60 in lst7
"manzana" in lst11


tpl1=(45, 78,12,9+3j,3.6)   #En las tuplas solo se puede utiizar operaciones inmutables
print(tpl1)

tpl2="Elemento1",45,3.89
type(tpl2)
print(tpl2)

tpl3=tuple(str1)
print(tpl3)

tpl4=tuple(lst7)
print(tpl4)

tpl4[0]

del(tpl4[0])

max(tpl4)


lst2=list(tpl2)
print(lst2)

lst2[0]="Cambio SRT"      #Las listas se pueden modificar, las tuplas no
print(lst2)


dic1={"elem1":32,"elem2":5.6,"val0":"Texto1","Val2":8+21j}
print(dic1)
type(dic1)

dic1["elem1"]

dic2={}
dic2["0"]=32
dic2["1"]=1087
dic2["2.1"]=19.92
dic2["ref1"]="PRIMER STR"
dic2["ref10"]=8-95j
dic2["lst11"]=["lunes","martes","miercoles"]
dic2["tpl15"]=["enero",12,365]
print(dic2)

dic2["lst11"]    #En el diccionario siempre le llamo a los elementos como strings
dic2["lst11"][1]

dic3=dict(nom1="Alejo", nom2=40, nom3=23.134)
print(dic3)

dic4=dict(zip("TEXTO",[4,7,1,3,1]))
print(dic4)

dic4=dict(zip("TEXTO",[4,7,1,3,1,6]))    #No sobreescribe el valor, solo lee el key word
print(dic4)

dic4=dict(zip("TEXTOABCD",[4,7,1,3,1,6]))
print(dic4)

zip("texto",[8,5,7,8,2])
print(zip("texto",[8,5,7,8,2]))

list(zip("texto",[8,5,7,8,2]))

list(zip("texto",[8,5,7,8,2],[9.1,4.6,3.2,7.8,10.9]))  #Crea tuplas para construir el arreglo

dict(zip("TEXTO",[8,5,7,8,2]))       #Es diferente al zip

dic4.items()


dicc3={"Tema1":"CCNN","area2":67,"name4":12.78,"45":[78,12,"prueba"]}
print(dicc3)

dicc3.keys()
list(dicc3.keys())

dicc3.values()

dicc3.values()

dicc3.clear()

dicc3={"Tema1":"CCNN","area2":67,"name4":12.78,"45":[78,12,"prueba"]}

dicc4=dicc3.copy()
print(dicc4)

dicc5=dicc4
print(dicc5)

dicc5 is dicc4    #Aquí son el mismo objeto

dicc4 is dicc3    #Aquí son objetos diferentes

dicc3.get("Tema1")
dicc3.get("name4")
dicc3.get("name")

dicc10={"Tema1":"Ciencia","area2":"MT","45":[78,12],"NUEVO":9673}

dicc3.update(dicc10)
print(dicc3)




#Funciones

def mostrar():
        """Documentación de la función"""
        print("MENSAJE DE PRUEBA DE FUNCIÓN")
mostrar()


def mostrar_nombre(nom1):
    """Documentación de la función
    Líneas adicionales de explicación"""
    print(f"Buenos dias,{nom1.upper()}")
    return

mostrar_nombre("Alejo")
mostrar_nombre("Roberto")
mostrar_nombre("Ximena")
mostrar_nombre("Cristina")
mostrar_nombre("Pedro")


def datos(nombre,apellido,edad):
    """Declarar el nombre y el apellido como un string
    y la edad como un int"""
    print(f"Nombre: {nombre.title()}\nApellido: {apellido.title()}\tEdad: {edad}")
    return

datos("cristina","cevallos",34)


#Ejercicio

#Escribir un programa basado en una función que permita validar que el argumento 
#ingresado a la función es un string, caso contrario que muestre en pantalla un mensaje 
#indicando que no es un string

def validarstr(param1):
    """Esta función valida que lo ingresado sea un str"""
    if isinstance(param1, str):
        print(f"Este dato: {param1} Sí es un string")
    else:
        print(f"Este dato: {param1} No es un string")
    return

validarstr("Texto1")
validarstr(78)



def validarstr(param1):
    """Esta función valida que lo ingresado sea un str o un int"""
    if isinstance(param1, str):
        print(f"Este dato: {param1} Sí es un string")
        return
    elif isinstance(param1, int):
        print(f"Este dato: {param1} Sí es un int")
        return
    else:
        print(f"Este dato: {param1} No es un string y No es un int")
        return

validarstr("Texto1")
validarstr(78.56)



def validarstring(string1):
    if type(string1)==str:
        print(f"{string1} es un string")
        return
    else:
        print("No es un string")
        return


validarstring("Texto1")



var1=input("Ingrese un dato: ")    #input siempre va a devolver como tipo de dato un string
validarstring(var1)




def datos(nombre,apellido,edad=0):
    """Declarar el nombre y el apellido como un string
    y la edad como un int"""
    print(F"Nombre: {nombre.title()}\nApellido: {apellido.title()}\tEdad: {edad}")
    return

datos("cristina","cevallos",34)



def adicion(num1, num2, num3):
    total=num1+num2+num3
    return total

print(adicion(4,5,6))

total1=(adicion(4,5,6))-67
print(total1)



def construccion(nombre,apellido):
    return (f"Nombre:{nombre}, Apellido:{apellido}")
    
print(construccion("Alejandro","Vargas"))


string1=construccion("Alejandro","Vargas")
print(string1.upper())


nom1="Alejandro"
ap1="Vargas"
string1=construccion(nom1,ap1)
print(string1.upper())











