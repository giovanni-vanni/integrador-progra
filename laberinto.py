import random
import pygame
def generarlaberinto(ancho, alto):
    # Ajustamos para que el laberinto tenga dimensiones impares
    if ancho % 2 == 0: ancho += 1
    if alto % 2 == 0: alto += 1

    # Inicializar con paredes
    laberinto = [[1 for _ in range(ancho)] for _ in range(alto)]

    # Direcciones posibles: arriba, abajo, izquierda, derecha
    direcciones = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    def es_valido(x, y):
        return 0 < x < alto-1 and 0 < y < ancho-1

    def cavar(x, y):
        laberinto[x][y] = 0  # marca como camino
        random.shuffle(direcciones)
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if es_valido(nx, ny) and laberinto[nx][ny] == 1:
                # cavamos el muro intermedio
                laberinto[x + dx//2][y + dy//2] = 0
                cavar(nx, ny)

    # Comienza desde una celda aleatoria impar
    inicio_x = random.randrange(1, alto, 2)
    inicio_y = random.randrange(1, ancho, 2)
    cavar(inicio_x, inicio_y)
    
    caminoslibres = [(i,j) for i in range(alto) for j in range(ancho) if laberinto[i][j] == 0] 
    keys = random.sample(caminoslibres,3) 
    for (x, y) in keys:
        laberinto[x][y] = 2

    return laberinto

def dibujarLaberinto(laberinto, screen):
    wall = pygame.image.load("assets/wall.png")
    wallcreeper = pygame.image.load("assets/wallcreeper.png")
    floor = pygame.image.load("assets/floor.png")
    key = pygame.image.load("assets/key.png")
    for i, fila in enumerate(laberinto):
        for j, columna in enumerate(fila):
            x = j * 40 
            y = i * 40
            if columna == 1:
                n = random.randint(0,1)
                if n == 1:
                    screen.blit(wall, (x, y))
                else:
                    screen.blit(wallcreeper, (x, y))
            else:
                screen.blit(floor, (x, y))
            
            if columna == 2:
                screen.blit(key, (x,y))
            
                