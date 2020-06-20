"""
@author: Rudik Roberto Rompich
@carnet: 19857
@clase: Herramientas Tecnologicas

Ejercicio 11 : Ortogonalización de Gram-Schmidt

"""

import numpy as np
import sympy

"""Esto es lo único que se debe editar"""
matriz= [[2,-1],[3,2]]



ejemplo= np.array(matriz)

def coeficiente(v,u):

    ui_= -((np.dot(v,u)/np.dot(u,u))*u)

    return ui_


def GramSchmidt(lista):

    dimension= len(lista)
    final= lista[0]
    for i in range(1, dimension):
        v= lista[i]

        for j in range(1,dimension):
            u= lista[j-1]
            coef=+ coeficiente(v,u)
            break

        operacion= v+coef

        final = np.vstack((final,operacion))

    return final

def normalizar(lista):

    normalizar = lista / np.sqrt(np.sum(lista**2))
    return normalizar



lol = int(input("\n|BIENVENIDO AL ORTOGONALIZADOR | \n" +

                "SELECCIONE UNA ACCIÓN PARA REALIZAR: \n\n" +
                "1. REALIZAR OPERACIÓN DE ORTOGANALIZAR VECTORES \n\n" +
                "0. Salir \n\n" +
                "OPCIÓN:"))

while lol != 0:

    if lol == 1:

        print("La matriz se puede editar al principio del código\n"+
              "Matriz ortogonalizada: \n")
        print(GramSchmidt(ejemplo))
        print("\n\nMatriz ortonormal: \n")
        print(normalizar(GramSchmidt(ejemplo)))



    else:

        print("Vuelva a ingresar un valor válido")

    lol = int(input("\n|BIENVENIDO AL ORTOGONALIZADOR | \n" +

                    "SELECCIONE UNA ACCIÓN PARA REALIZAR: \n\n" +
                    "1. REALIZAR OPERACIÓN DE ORTOGANALIZAR VECTORES \n\n" +
                    "0. Salir \n\n" +
                    "OPCIÓN:"))
