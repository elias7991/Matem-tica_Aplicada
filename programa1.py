#****MATEMÁTICA APLICADA****
#Desarrollo de la aplicación correspondiente a la actividad 2.3
'''
Integrantes:
    - Elías Santiago Cáceres Melgarejo, 5.437.101
    - Ever Fernando Garay Molinas. 

'''

#Tema: Desarrollo de una calculadora de números difusos triangulares

#Desarrollo del código fuente

#Importación de paquetes útiles
import os
import pylab as pl
import numpy as np

#Definir funcion de borrado de pantalla
def borrar_pantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

#Validacion de un numero entero entre 1 y 5
def validar_entrada():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduzca su opción (1,2,3,4 o 5): "))
            if (num >= 1 and num <= 5 ):
                correcto=True
            else:
                print("Error, la opción ingresada no está entre 1 y 5")
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num

#Validacion de numero positivo
def validar_no_negativo():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input())
            if (num < 0):
                print('Error, introduce un numero no negativo')
            else:
                correcto=True
        except ValueError:
            print("Error, introduzca un número")
    return num

#Validar número difuso triangular tfn=(a,b,c)
def validar_triangular():

    print("Ingrese el núcleo: ")
    a = validar_no_negativo()

    print("Ingrese e_l: ")
    b = validar_no_negativo()
    while (b <= 0):
        print("Error, e_l debe de ser mayor a cero")
        print("Ingrese e_l: ")
        b = validar_no_negativo()

    print("Ingrese e_r: ")
    c = validar_no_negativo()
    while (c <= 0):
        print("Error, e_r debe de ser mayor a cero")
        print("Ingrese e_r: ")
        c = validar_no_negativo()

    #usamos tupla debido a que debe ser ordenado e inalterable
    tfn = (a,b,c)

    return tfn

#Graficar número difuso triangular
def grafico_triangular(tfn):
    #Partiremos por definir los dominios de los trozos
    X = np.linspace(tfn[0]-tfn[1]-2, tfn[0]-tfn[1], 256, endpoint=True)
    Y = np.linspace(tfn[0]-tfn[1], tfn[0], 256, endpoint=True)
    W = np.linspace(tfn[0], tfn[0]+tfn[2], 256, endpoint=True)
    Z = np.linspace(tfn[0] + tfn[2], tfn[0] + tfn[2] + 2, 256, endpoint=True)

    A, B, C, D = 0*X, ( 1 + ( (Y - tfn[0])/(tfn[1]) ) ), ( 1 - ( (W - tfn[0])/(tfn[2]) ) ), 0*Z

    pl.plot(X,A)
    pl.plot(Y,B)
    pl.plot(W,C)
    pl.plot(Z,D)

    pl.show()


#Adición entre números difusos triangulares
def op_adicion():

    borrar_pantalla()  

    print("Sumar dos números difusos triangulares".center(50," "))
    print("Un número difuso triangular tiene la forma: tfn = (a,b,c)")
    print("a: núcleo")
    print("b: longitud desde el núcleo hasta la función a la izquierda")
    print("c: longitud desde el núcleo hasta la función a la derecha")

    print("Ingrese el primer sumando A")
    A = validar_triangular()
    print("Ingrese el segundo sumando B")
    B = validar_triangular()
    
    suma = tuple(sum(x) for x in zip(A,B))
    print("El número difuso triangular resultante es: ", suma)

    print("Grafico de A".center(50,"*"))
    grafico_triangular(A)

    print("Grafico de B".center(50,"*"))
    grafico_triangular(B)

    print("Grafico de la suma".center(50,"*"))
    grafico_triangular(suma)

#Sustracción entre números difusos triangulares
def op_sustraccion():

    borrar_pantalla()

    print("Restar dos números difusos triangulares".center(50," "))
    print("Un número difuso triangular tiene la forma: tfn = (a,b,c)")
    print("a: núcleo")
    print("b: longitud desde el núcleo hasta la función a la izquierda")
    print("c: longitud desde el núcleo hasta la función a la derecha")

    print("Ingrese el minuendo A")
    A = validar_triangular()
    print("Ingrese el sustraendo B")
    B = validar_triangular()

    #Comprobar que los números difusos triangulares sean correctos para la sustraccion.
    while (A[1]-B[2] < 0 or A[2]-B[1] < 0):
        borrar_pantalla()
        
        print("Error, los valores ingresados no son válidos para realizar la resta.")
        print("Sugerencia".center(100,"*"))
        print("Dado (3,3,2)-(1,2,1) = (3-1,3-1,2-2) = (2,2,0)")
        print("Como ve, los valores de e_l y e_r deben resultar no negativos")

        print("Ingrese el minuendo A")
        A = validar_triangular()
        print("Ingrese el sustraendo B")
        B = validar_triangular()

    resta = (A[0]-B[0],A[1]-B[2],A[2]-B[1])
    print("El número difuso triangular resultante es: ", resta)

    print("Grafico de A".center(50,"*"))
    grafico_triangular(A)

    print("Grafico de B".center(50,"*"))
    grafico_triangular(B)

    print("Grafico de la resta".center(50,"*"))
    grafico_triangular(resta)

#Multiplicación entre números difusos triangulares
def op_multiplicacion():

    borrar_pantalla()
    print("Multiplicar dos números difusos triangulares".center(50," "))
    print("Un número difuso triangular tiene la forma: tfn = (a,b,c)")
    print("a: núcleo")
    print("b: longitud desde el núcleo hasta la función a la izquierda")
    print("c: longitud desde el núcleo hasta la función a la derecha")

    print("Ingrese el multiplicando A")
    A = validar_triangular()
    print("Ingrese el multiplicando B")
    B = validar_triangular()

    producto = (A[0]*B[0], min( A[1]*B[1], A[1]*B[2], A[2]*B[1], A[2]*B[2] ), max( A[1]*B[1], A[1]*B[2], A[2]*B[1], A[2]*B[2] ))
    print("El número difuso triangular resultante es: ", producto)

    print("Grafico de A".center(50,"*"))
    grafico_triangular(A)

    print("Grafico de B".center(50,"*"))
    grafico_triangular(B)

    print("Grafico de la resta".center(50,"*"))
    grafico_triangular(producto)

#División entre números difusos
def op_dividir():

    borrar_pantalla()
    
    print("Dividir dos números difusos triangulares".center(50," "))
    print("Un número difuso triangular tiene la forma: tfn = (a,b,c)")
    print("a: núcleo")
    print("b: longitud desde el núcleo hasta la función a la izquierda")
    print("c: longitud desde el núcleo hasta la función a la derecha")

    print("Ingrese el Dividendo A")
    A = validar_triangular()
    print("Ingrese el Divisor B")
    B = validar_triangular()

    while ( B[0] == 0 or B[1] == 0 or B[2] == 0 ):
        
        print("Error, el número difuso triangular no debe poseer ninguna componente nula.")
        print("Ingrese nuevamente el Divisor B")
        B = validar_triangular()

    division = (A[0]/B[0], min( A[1]/B[1], A[1]/B[2], A[2]/B[1], A[2]/B[2] ), max( A[1]/B[1], A[1]/B[2], A[2]/B[1], A[2]/B[2] ))
    print("El número difuso triangular resultante es: ", division)

    print("Grafico de A".center(50,"*"))
    grafico_triangular(A)

    print("Grafico de B".center(50,"*"))
    grafico_triangular(B)

    print("Grafico de la división".center(50,"*"))
    grafico_triangular(division)

#desarrollo del menú
def menu():
    #por defecto para ingresar al while
    opcion = 0
    while (opcion != 5):

        #Para cualquier sistema operativo
        borrar_pantalla()

        saludo = "Bienvenido a la calculadora difusa."
        print(saludo.center(50, " "))

        pregunta = "¿Qué desea realizar?"
        print("\n",pregunta.center(50, " "), "\n")

        print("1.-Adición.")
        print("2.-Sustracción.")
        print("3.-Multiplicación.")
        print("4.-División.")
        print("5.-Salir.")
        #una opcion NO NUMERICA no será admitida.
        opcion = validar_entrada()

        if(opcion == 1):
            op_adicion()
            os.system('pause')
        if(opcion == 2):
            op_sustraccion()
            os.system('pause')
        if(opcion == 3):
            op_multiplicacion()
            os.system('pause')
        if(opcion == 4):
            op_dividir()
            os.system('pause')

menu()