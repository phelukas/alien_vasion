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

    # Criando uma espaçonave
    ship = Ship(ai_settings, screen)

    # Cria um grupo na qual serão armazenados os projéteis
    bullets = Group()

    # Define a cor de fundo 
    bg_color = (230, 230, 230)

    # Cria um alienígina
    alien = Alien(ai_settings, screen)

    # Inicializa o laço principal do jogo
    while True: 

        # Observa eventos do teclado e do mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()

        # Gerenciador dos tiros
        gf.update_bullets(bullets)

        # Gerenciador de alieníginas
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

        # Redesenha a tela a cada passagem pelo laço
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

        # Deixa a tela mais recente visível
        pygame.display.flip()   

run_game()
