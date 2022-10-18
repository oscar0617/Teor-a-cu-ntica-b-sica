# TEORÍA CUÁNTICA BÁSICA, OBSERVABLES Y MEDIDAS

_En esta libreria encontraremos la solución a diferentes ejercicios planteados en el libro Quatum Computer for Computer Sciencist_
1. Calcular la probabilidad de que se encuentre una particula en una posición.
2. Calcular la probabilidad de que la particula salte de un vector a otro.
3. Calcular la amplitud de transición.
4. Calcular la media y la varianza.
5. Calcular los valores y vectores propios.
6. Calcular el estado final.
7. Ejercicio 4.3.1
8. Ejercicio 4.3.2
9. Ejercicio 4.4.1
10. Ejercicio 4.4.2

### Pre-requisitos
_Para poder correr nuestra libreria necesitaremos un iDLE cualquiera de python._\
_Para poder obtener un resultado exitoso debemos tener la libreria de numpy instalados en python, de lo contrario no podremos ejecutar satisfactoriamente nuestras funciones._ \

### Ejemplos
_A continuación encontraremos el ejemplo de la función de Varianza:_
```
def varianza(observable, vectorEstado):
    media_ = media(observable, vectorEstado)
    identidad = np.identity(len(vectorEstado))
    mediaIdentidad =media_ * np.matrix(identidad)
    resta = np.matrix(observable) - np.matrix(mediaIdentidad)
    multiplicacion = np.matrix(resta).dot(np.matrix(resta))
    res = media(multiplicacion, vectorEstado)
    return res
```
_¿Cómo podemos verificar estos resultados?_\
_Primero debemos obtener la media entre el observable y el vector estado mendiante la siguiente función:_
```
def media(observable, vectorEstado):
    esHermitiana = hermitiana(observable)
    if esHermitiana == True:
        if np.linalg.norm(vectorEstado) != 1:
            vectorEstado = normalizarVector(vectorEstado)
        productoMatrizVector = matrizPorVector(observable, vectorEstado)
        media = productoInterno(productoMatrizVector, vectorEstado)
    return media
```
_Luego vamos a fabricar nuestra matriz identidad utilizando la libreria de Numpy y realizaremos la resta de estas dos matrices. Luego vamos a multiplicar lo que nos dio de la resta con si misma, y por ultimo vamos a realizar la media entre este ultimo paso con el vector Estado dado inicialmente._

### Pruebas en codigo
_Al finalizar cada función encontraremos su respectiva prueba con comentario (```#print(media([[1,-1j], [1j,2]],[math.sqrt(2)/2,(math.sqrt(2)/2)*1j]))```), para poder probar cada una debemos quitar sus respectivos comentarios._

## ¿Como lo construimos?
* [Pycharm](https://www.jetbrains.com/es-es/pycharm/) -_El iDLE usado_

## Autor
* **Oscar Lesmes** - *Libreria completa* - [GitHub](https://github.com/villanuevand)

