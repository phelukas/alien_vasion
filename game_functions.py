from bullet import Bullet

import sys
import pygame


def check_events(ai_settings, screen, ship, bullets):
    """Responde a eventos de pressionamento de teclas e mouse"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde a pressionamento de tecla"""

    # Move a espaçonave para direita
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    # Move a espaçonave para esquerda
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    # Cria um novo projétil e o adiciona ao grupo de projéteis
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Responde a solturas de teclas"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
            
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    """Atualiza as imagens na tela e altera para a nova tela."""

    # Redesenha a tela a casa passagem pelo laço
    screen.fill(ai_settings.bg_color) 

    # Redesenha todos os projéteis atrás da espaçonave e das alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

def update_bullets(bullets):
    """"Atualiza a posição dos projéteis e se livra dos projéteis antigos."""

    # Atualiza as posições dos projéteis
    bullets.update()

    # Livra-se dos projéteis que desaparecem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara um projétil se o limite ainda não foi alcançado"""

    # Cria um novo projétil e o adciona ao grupo de projéteis
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)    
