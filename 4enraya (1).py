#!/usr/bin/env python
# coding: utf-8

# In[5]:


### import pygame
import numpy as np


def imprimirTablero(tablero):
    for i in tablero:
        print(i)

def ganador(tablero, jugador):
    winner=False
    for i in range(filas):
        winner=4*jugador in''.join(tablero[i,:]) #join coge los elementos de asd y los concatena poniendo entre ellos ''
        if winner==True:
            return winner 
    for i in range(columnas):
        winner=4*jugador in''.join(tablero[:,i]) #join coge los elementos de asd y los concatena poniendo entre ellos ''
        if winner==True:
            return winner
    return winner
        
        
#filas=input("Escoja el numero de filas: ")
#columnas=input("Escoja el numero de columnas: ")
#filas=int(filas)
#columnas=int(columnas)

filas, columnas = 3, 4

tablero=np.array([[' ' for _ in range(columnas)] for _ in range(filas)]) #se genera una matriz de strings con un espacio
imprimirTablero(tablero)

casillasLibres=[filas for i in range(columnas)]   #este for te indica la longitud del vector y en esa posicion(columna) las casillas libres 

jugador='OX①②③④⑤' #strings

numJugadores=2
while numJugadores>7 or numJugadores<2:
    
    numJugadores=input("Número de jugadores") #input te devulve string
    numJugadores=int(numJugadores)
   
    if numJugadores>7 or numJugadores<2:
        print("Excede el numero máximo de jugadores ")

for i in range(numJugadores):
    print(jugador[i])
winner2=False   
turno=0
columnaJugador=-1
while(winner2==False):
    columnaJugador=int(input(f"Jugador {jugador[turno]} Escoge una columna: "))-1
    while columnaJugador>columnas or columnaJugador<0 or casillasLibres[columnaJugador]<=0:
        columnaJugador=int(input(f"Jugador {jugador[turno]} Escoge una columna: "))-1 #f formatear una cadena
    
    
    
    tablero[casillasLibres[columnaJugador]-1,columnaJugador]=jugador[turno]
    imprimirTablero(tablero)
    winner2=ganador(tablero, jugador[turno])
    
    casillasLibres[columnaJugador]=casillasLibres[columnaJugador]-1
    
    turno=(turno+1)%numJugadores
    
    
  


# In[20]:


def imprimirTablero(tablero):
    for i in tablero:
        print(i)
        


# In[4]:


def ganador(tablero, jugador):
    winner=False
    for i in range(filas):
        winner=4*jugador in''.join(tablero[i,:]) #join coge los elementos de asd y los concatena poniendo entre ellos ''
        if winner==True:
            return winner 
    for i in range(columnas):
        winner=4*jugador in''.join(tablero[:,i]) #join coge los elementos de asd y los concatena poniendo entre ellos ''
        if winner==True:
            return winner
    return winner


# In[ ]:




