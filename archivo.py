#De tipo primitivo

nombre = "Dennis"   #String
edad = 33           #int
estatura = 1.71     #float
buceo = False       #booleano

resultado = (nombre) +" "+str(edad) +" "+str(estatura) +" "+str(buceo) #con str se convierte a string las variables numericas
print(resultado)




"""Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de 
tipo entero y almacenar el resultado en una variable"""

print("Ingrese el primer numero: ")
n1 = int(input())
print("ingrese el ultimo numero:")
n2 = int(input())

suma = 0

while   n1 <= n2:
    if  n1 % 2 == 0:
        print(n1)
        suma = suma+n1
    n1+=1
print(f"La suma de los numeros pares es : {suma}")










#Investiga sobre el límite de los enteros y los flotantes en python y
# anotar sus descubrimientos como comentarios en el archivo
""""
En Python, los enteros y los flotantes son dos tipos de datos numéricos utilizados para representar números. 
Ambos tipos de datos tienen límites en cuanto al rango de valores que pueden representar. A continuación,
 te proporciono información sobre los límites de enteros y flotantes en Python:

Límites de enteros (integers):

Python 3 utiliza un sistema de representación de enteros que permite representar enteros de longitud variable, 
es decir, los enteros pueden crecer en tamaño según sea necesario. Esto significa que no hay un límite fijo en
 cuanto al valor máximo o mínimo de un entero en Python 3. En lugar de tener un valor máximo fijo como en otros 
 lenguajes de programación, Python 3 puede manejar enteros de gran tamaño hasta que alcancen los límites impuestos
  por la memoria disponible en la máquina.

En Python 2, los enteros están representados por un tipo llamado "long" cuando superan el rango de un entero normal.
 Los enteros de Python 2 tienen un límite, que está determinado por la cantidad de memoria disponible y puede 
 variar según la plataforma y la versión de Python 2 utilizada.

Límites de flotantes (float):

Python utiliza el estándar IEEE 754 para representar números de punto flotante. Este estándar define diferentes 
formatos de representación para flotantes, como 32 bits (float) y 64 bits (double).
Para flotantes de 32 bits (float), el rango de representación es aproximadamente de ±3.4e-38 a ±3.4e38. Es decir, 
pueden representar números muy pequeños cercanos a cero y números muy grandes cercanos a ±3.4e38.
Para flotantes de 64 bits (double), que es el tipo de flotante predeterminado en Python, el rango de representación
 es mucho mayor, aproximadamente de ±1.7e-308 a ±1.7e308. Por lo tanto, los flotantes de 64 bits pueden 
 representar números extremadamente pequeños cercanos a cero y números extremadamente grandes cercanos a ±1.7e308.

Es esencial tener en cuenta que, debido a las limitaciones de precisión inherentes a los números de punto flotante,
 pueden ocurrir errores de redondeo en ciertos cálculos.

En resumen, Python no tiene límites fijos para enteros debido a su capacidad para manejar enteros de longitud 
variable. Para flotantes, los límites están determinados por el estándar IEEE 754 y varían según el tamaño del tipo
 de flotante utilizado (32 o 64 bits).
 """

