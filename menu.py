from tkinter import font
import pygame
from math import floor

# Función para mostrar menú principal
def mostrarMenuPrincipal(screen, clock):
    menu_fondo = pygame.image.load('assets/BackgroundMain.jpeg')
    menu_fondo = pygame.transform.scale(menu_fondo, (760, 760))
    
    # Crear botón "Jugar"
    boton_rect = pygame.Rect(760 // 2 - 75, 760 // 2 + 100, 150, 50)
    font = pygame.font.Font(None, 36)

    menu_activo = True
    while menu_activo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_rect.collidepoint(event.pos):
                    menu_activo = False
        
        # Dibujar fondo
        screen.blit(menu_fondo, (0, 0))
        
        # Dibujar botón
        pygame.draw.rect(screen, (100, 150, 255), boton_rect)
        texto = font.render('Jugar', True, (255, 255, 255))
        texto_rect = texto.get_rect(center=boton_rect.center)
        screen.blit(texto, texto_rect)

        titulo = font.render("LABERINTO DEL DESAFIO", True, (0, 0, 0))
        screen.blit(titulo, (240, 180))
        
        pygame.display.flip()
        clock.tick(60)

# Función para mostrar menú
def mostrarMenuFinal(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.SysFont(None, 80)
    titulo = font.render("FELICIDADES ESCAPASTE", True, (255, 255, 255))
    screen.blit(titulo, (420, 150))