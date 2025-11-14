import pygame
from math import floor

# Función para mostrar menú
def mostrarMenu(screen, clock):
    global running
    menu_fondo = pygame.image.load('assets/BackgroundMain.jpeg')
    menu_fondo = pygame.transform.scale(menu_fondo, (1240, 680))
    
    # Crear botón "Jugar"
    boton_rect = pygame.Rect(1240 // 2 - 75, 680 // 2 + 100, 150, 50)
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
        
        pygame.display.flip()
        clock.tick(60)