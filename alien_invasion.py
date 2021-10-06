from pygame.sprite import Group
from settings import Settings
from alien import Alien
from ship import Ship

import game_functions as gf
import pygame


def run_game():
    
    # Inicializa o jogo, com as config. do settings
    pygame.init()  
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )   
    pygame.display.set_caption("Alien Invasion")   

    # Define a cor de fundo 
    bg_color = (230, 230, 230) 
    
    # Criando uma espaçonave
    ship = Ship(ai_settings, screen)

    # Cria um grupo na qual serão armazenados os projéteis
    bullets = Group()

    # Cria um grupo na qual serão armazenados os alienígenas
    aliens = Group()

    # Cria uma frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Inicializa o laço principal do jogo
    while True: 

        # Observa eventos do teclado e do mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()

        # Gerenciador dos tiros
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

        # Gerenciador dos aliens
        gf.update_aliens(ai_settings, aliens)

        # Gerenciador de alieníginas
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
