from math import floor
import random
import pygame
import os
from laberinto import generarlaberinto , dibujarLaberinto, generarSalida

pygame.init()
screen = pygame.display.set_mode((1240, 680))
clock = pygame.time.Clock()
running = True
dt = 0
speed = 1

start_row = 1
start_col = 1

# Control de animacion
moving_left = False
moving_right = False
walk_count = 0

# Cargar y escalar imágenes de caminata (40x40)
walk_right_path = [pygame.transform.scale(pygame.image.load(f'assets/(R)player{i}.png').convert_alpha(), (40, 40)) for i in range(1, 5)]
walk_left_path = [pygame.transform.scale(pygame.image.load(f'assets/(L)player{i}.png').convert_alpha(), (40, 40)) for i in range(1, 5)] 

stand_right = pygame.transform.scale(pygame.image.load('assets/(R)player2.png').convert_alpha(), (40, 40))
stand_left = pygame.transform.scale(pygame.image.load('assets/(L)player2.png').convert_alpha(), (40, 40))

standing = stand_right
floor_imagen = pygame.image.load('assets/floor.png').convert_alpha()
class Player():
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/(L)player2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.col = x
        self.row = y
        self.keys = 0
        self.allKeysCollected = False

    def draw(self, screen):
        x = self.col * 40
        y = self.row * 40
        screen.blit(self.image, (x, y))

    def move(self, dx, dy):
        # Movimiento en términos de celdas del laberinto
        new_col = self.col + dx 
        new_row = self.row + dy 

        # Verificar límites y colisión: actualizar solo si la celda es camino (0)
        if 0 <= new_row < len(level) and 0 <= new_col < len(level[0])  :
            cell = level[new_row][new_col] 
            if cell == 0:
                self.col = new_col
                self.row = new_row
            elif cell == 2:
                self.col = new_col
                self.row = new_row
                self.keys += 1
                if self.keys == 3:
                    self.allKeysCollected = True
                level[new_row][new_col] = 0
                # Borrar solo la celda de la llave en el background
                rect = pygame.Rect(new_col * 40, new_row * 40, 40, 40)
                background.blit(floor_imagen, (new_col * 40, new_row * 40))
            
        if self.allKeysCollected == True:
            generarSalida(31, 17, level, background)
            self.allKeysCollected = False
            

level = generarlaberinto(31,17)

# Dibujar el laberinto una sola vez en una superficie de fondo
background = pygame.Surface(screen.get_size())
dibujarLaberinto(level, background)

# Asegurar que la posición inicial esté en una celda libre (0)
if level[start_row][start_col] != 0:
    found = False
    for i, fila in enumerate(level):
        for j, val in enumerate(fila):
            if val == 0:
                start_row = i
                start_col = j
                found = True
                break
        if found:
            break

PLAYER = Player(start_col, start_row)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del jugador (teclas mantenidas permiten movimiento continuo)
    keys = pygame.key.get_pressed()
    moving_left = False
    moving_right = False

    if keys[pygame.K_w]:
        PLAYER.move(0, -1)
    if keys[pygame.K_s]:
        PLAYER.move(0, 1)
    if keys[pygame.K_a]:
        PLAYER.move(-1, 0)
        moving_left = True
    if keys[pygame.K_d]:
        PLAYER.move(1, 0)
        moving_right = True

    # Actualizar contador de pasos
    if moving_left or moving_right:
        walk_count = (walk_count + 1) % len(walk_right_path)
    else:
        walk_count = 0

    # Dibujar: blit del fondo (laberinto) y luego el jugador (frame correcto)
    screen.blit(background, (0, 0))

    if moving_left:
        PLAYER.image = walk_left_path[walk_count]
        standing = stand_left
    elif moving_right:
        PLAYER.image = walk_right_path[walk_count]
        standing = stand_right
    else:
        PLAYER.image = standing

    PLAYER.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) /1000

pygame.quit()
