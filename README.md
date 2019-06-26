# Codewars kata student correction IH

## Importante

Revisar el timezone porque hay desfase -> consola > Date.now()

## Intro

¿Estás cansado de tener que mirar a la pizarra para comprobar si tus alumnos han terminado la kata a tiempo? ¿Te apetece seguir flipando con la web de D3 en vez de girar el cuello hasta esa corta lista de estudiantes que han completado esa kata tan fácil? ¿Deseando que alguien haga el trabajo por tí? ¿Por programación?

Este código te cambiará la vida en este aspecto, del resto de tu vida ya te encargas tu. 

## Descripción

Este software permite comprobar el progreso de los alumnos y sus tiempos en codewars. Está compuesto por varios archivos CSV y unos ficheros de código en Python que harán todo el trabajo. 


## Instrucciones

### Carpeta input
#### katas.csv
Encontrarás algo así. 
```
slug,date,minutes
regexp-fun-number-1-when-i-miss-few-days-of-gym,2019-02-01T16:20:21.241Z,60
deodorant-evaporator,2019-02-01T16:20:21.241Z,60
ordered-count-of-characters,2019-02-13T10:00:00.241Z,45
```
Solo deberás crear el contenido en función de las katas que hayas enviado, cuando las hayas enviado y el tiempo que les has dado para resolverla. 
La primera linea son los nombres de los campos de cada kata que envías. 
1. slug: La URL de una kata cualquiera es `https://www.codewars.com/kata/replace-with-alphabet-position/train/python`, su slug es `replace-with-alphabet-position`. 
2. date. Escrito en formato Datetime de la librería pandas
3. minutes. Cantidad de tiempo en minutos que tienen para resolver. 

NOTAS: 
1. Si se empieza el CSV con solo una kata, dará fallo, poned 2. 


#### students.csv
Encontrarás algo así. 
```
name,username
Paula Postigo Rodrigo,paulapr
Almudena Gonzalez Salcedo,Almugs
Héctor Moreno Álvarez,hector-moreno
```
Solo deberás modificar el contenido para que corresponda con el nombre y el usuario de codewars de ese estudiante. 

### Carpeta source
Contiene un fichero `main.py` que resolverá todo. 


## API
```
# https://www.codewars.com/api/v1/users/Livia Canet/code-challenges/completed
```




