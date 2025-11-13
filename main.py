import random
import pygame
import os
from laberinto import generarlaberinto , dibujarLaberinto

pygame.init()
screen = pygame.display.set_mode((1240, 680))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

class Player():
    def draw(self,screen):
            screen.blit(self.quieto, player_pos)
    def __init__(self):
        self.quieto = pygame.image.load('assets/(L)player2.png')

PLAYER = Player()
level = generarlaberinto(31,17)
dibujarLaberinto(level, screen)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    PLAYER.draw(screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    
    pygame.display.flip()

    
    dt = clock.tick(60) / 1000

pygame.quit()
