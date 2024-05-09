import numpy as np
import pygame
import sys


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
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
NARANJA = (255, 165, 0)
MAGENTA = (255, 0, 255)
CIAN = (0, 255, 255)
GRIS = (128, 128, 128)
jugador='OX①②③④⑤' #strings
colores=[ROJO, VERDE , AMARILLO , NARANJA , MAGENTA , CIAN , GRIS] #rojo, verde, azul RGB
        
filas=input("Escoja el numero de filas: ")
columnas=input("Escoja el numero de columnas: ")
filas=int(filas)
columnas=int(columnas)

numJugadores=1
while numJugadores>7 or numJugadores<2:
    
    numJugadores=input("Número de jugadores") #input te devulve string
    numJugadores=int(numJugadores)
   
    if numJugadores>7 or numJugadores<2:
        print("Excede el numero máximo de jugadores ")




WIDTH = 640
HEIGHT = 480
ROWS = filas
COLS = columnas
SQUARE_SIZE = 80

tablero=np.array([[' ' for _ in range(columnas)] for _ in range(filas)]) #se genera una matriz de strings con un espacio
#imprimirTablero(tablero)

casillasLibres=[filas for i in range(columnas)]   #este for te indica la longitud del vector y en esa posicion(columna) las casillas libres 
# Colores
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) #1a componente cuadrado del tamaño indicado en col, 2a cuadrado en fila, tamaño1, tamaño2
            pygame.draw.circle(screen, BLACK, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), int(SQUARE_SIZE / 2 - 5))


running = True
draw_board()
pygame.display.update()

turno=0
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #una vez picamos la cruz nos salimos,
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            # Obtener la posición del mouse en el momento del clic
            mouse_pos = pygame.mouse.get_pos()
            columnaJugador=mouse_pos[0]//SQUARE_SIZE
            if columnaJugador<columnas and casillasLibres[columnaJugador]>0:   
                tablero[casillasLibres[columnaJugador]-1,columnaJugador]=jugador[turno]
                imprimirTablero(tablero)
                pos=(columnaJugador * SQUARE_SIZE + SQUARE_SIZE // 2, 
                                                           (casillasLibres[columnaJugador]-1)* SQUARE_SIZE + SQUARE_SIZE // 2)
                print (pos)
                pygame.draw.circle(screen, colores[turno], pos, SQUARE_SIZE // 2 - 5)
                pygame.display.update()
                
                
    
                casillasLibres[columnaJugador]=casillasLibres[columnaJugador]-1
                winner2=ganador(tablero, jugador[turno])
                if winner2==True:
        
                    pygame.quit()
                    
                turno=(turno+1)%numJugadores

            
                                

pygame.quit()