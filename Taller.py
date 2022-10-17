# -*- coding: utf-8 -*-
"""
Created on Tue 27 11:45:54 2022
@author: Oscar Lesmes
"""
import math
import numpy as np

def probabilidad(vector, posicion):
    """
    Da la probabilidad de posicion dado un vector
    (list) -> float
    """
    normaCuadrado = 0
    for i in vector:
        normaCuadrado += abs(i) ** 2
    conjugado = (abs(vector[posicion]))**2
    probabilidadPosicion = conjugado / normaCuadrado
    return probabilidadPosicion

#print(probabilidad([2+1j,-1+2j, 1j, 1+0j, 3-1j, 2+0j, -2j, -2+1j, 1-3j, -1j],10))

def amplitudTransicion(vector1, vector2):
    """
    Da la amplitud de transición entre dos vectores
    (list, list) -> complex
    """
    norma1 = np.linalg.norm(vector1)
    norma2 = np.linalg.norm(vector2)
    for i in range(len(vector1)):
        vector1[i] = vector1[i] / norma1
        vector2[i] = vector2[i] / norma2

    productoInterno = 0
    for i in range(len(vector1)):
        productoInterno += vector2[i] * vector1[i]

    productoVectores = norma1 * norma2
    probabilidad = productoInterno / productoVectores
    return probabilidad

#print(amplitudTransicion([1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0]))

def hermitiana(matriz):
    matrizConjugada = np.conjugate(matriz)
    return np.array_equal(matriz, np.transpose(matrizConjugada))

def normalizarVector(vector):
    norma = np.linalg.norm(vector)
    for i in range(len(vector)):
        vector[i] = vector[i] / norma
    return vector

def matrizPorVector(matriz, vector):
    matriz = np.array(matriz)
    vector = np.array(vector)
    producto = matriz.dot(vector)
    return producto

def productoInterno(vector1, vector2):
    productointerno = 0
    for i in range(len(vector1)):
        productointerno += vector2[i] * vector1[i].conjugate()
    return productointerno

def media(observable, vectorEstado):
    esHermitiana = hermitiana(observable)
    if esHermitiana == True:
        if np.linalg.norm(vectorEstado) != 1:
            vectorEstado = normalizarVector(vectorEstado)
        productoMatrizVector = matrizPorVector(observable, vectorEstado)
        media = productoInterno(productoMatrizVector, vectorEstado)
    return media

#print(media([[1,-1j], [1j,2]],[math.sqrt(2)/2,(math.sqrt(2)/2)*1j]))

def varianza(observable, vectorEstado):
    media_ = media(observable, vectorEstado)
    identidad = np.identity(len(vectorEstado))
    mediaIdentidad =media_ * np.matrix(identidad)
    resta = np.matrix(observable) - np.matrix(mediaIdentidad)
    multiplicacion = np.matrix(resta).dot(np.matrix(resta))
    res = media(multiplicacion, vectorEstado)
    return res
#print(varianza([[1,-1j], [1j,2]],[math.sqrt(2)/2,(math.sqrt(2)/2)*1j]))

def valorPropio(matriz):
    matriz = np.array(matriz)
    valoresPropios = np.linalg.eigvals(matriz)
    return valoresPropios

def vectorPropio(matriz):
    valoresPropios, vectoresPropios = np.linalg.eig(matriz)
    return vectoresPropios

#Ejercicio 4.3.1

def ejercicio431(observable):
    spinup = np.array([1,0])
    valoresPropios = valorPropio(observable)
    vectoresPropios = vectorPropio(observable)
    vectoresPropios= normalizarVector(vectoresPropios)
    accionObservableVector = matrizPorVector(observable, spinup)
    res = probabilidad(accionObservableVector, 0)
    return res
#observable = [[0,1/2],[1/2,0]]
#print(ejercicio431(observable))

def ejercicio432(observable):
    spinup = np.array([1, 0])
    valoresPropios = valorPropio(observable)
    vectoresPropios = vectorPropio(observable)
    vectoresPropios = normalizarVector(vectoresPropios)
    accionObservableVector = matrizPorVector(observable, spinup)
    p1 = productoInterno(accionObservableVector, vectoresPropios[0])
    p1 = np.linalg.norm(p1)
    p2 = productoInterno(accionObservableVector, vectoresPropios[1])
    p2 = np.linalg.norm(p2)
    res = p1*valoresPropios[0] + p2*valoresPropios[1]
    return res
#observable = [[0,1/2],[1/2,0]]
#print(ejercicio432(observable))

def ejercicio441(matriz1, matriz2):
    identity  = np.identity(len(matriz1))
    checkunit1 = matriz1 * matriz1.conjugate()
    checkunit2 = np.round(matriz2 * matriz2.conjugate())
    if np.array_equal(checkunit1, identity) and np.array_equal(checkunit2, identity):
        matrizProducto = matriz1 * matriz2
        matrizProductoconjugada = matrizProducto.transpose()
        matrizProductofinal = np.round(matrizProducto * matrizProductoconjugada)
        identity2 = np.identity(len(matrizProducto))
        if np.array_equal(matrizProductofinal, identity2):
            return matrizProducto, True
    return False, False

matriz1 = np.matrix([[0,1], [1,0]])
matriz2 = np.matrix([[math.sqrt(2)/2, math.sqrt(2)/2 ], [math.sqrt(2)/2, -math.sqrt(2)/2]])


def ejercicio442(matriz, estado):
    matriz = np.array(matriz)
    matriz3 = matriz**3
    matrizEstado = matrizPorVector(matriz3,estado)
    res = probabilidad(matrizEstado, 3)
    return res

#matriz =[[0, 1/math.sqrt(2),1/math.sqrt(2),0],[1j/math.sqrt(2),0,0,1/math.sqrt(2)],[1/math.sqrt(2),0,0,1j/math.sqrt(2)],[0, 1/math.sqrt(2),-1/math.sqrt(2),0]]
#estado = [1,0,0,0]

#print(ejercicio442(matriz,estado))