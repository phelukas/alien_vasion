import sys
import pygame


def check_events(ship):
    """Responde a eventos de pressionamento de teclas e mouse"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    """Responde a pressionamento de tecla"""

    # Move a espaçonave para direita
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    # Move a espaçonave para esquerda
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """Responde a solturas de teclas"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
            
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na tela e altera para a nova tela."""

    # Redesenha a tela a casa passagem pelo laço
    screen.fill(ai_settings.bg_color)                
    ship.blitme()
