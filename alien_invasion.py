from settings import Settings
from ship import Ship

import pygame
import game_functions as gf


def run_game():
    # Inicializa o jogo, com as config. do settings
    pygame.init()  
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )   
    pygame.display.set_caption("Alien Invasion")   

    # Criando uma espaçonave
    ship = Ship(screen)

    # Define a cor de fundo 
    bg_color = (230, 230, 230)

    # Inicializa o laço principal do jogo
    while True: 

        # Observa eventos do teclado e do mouse
        gf.check_events()

        # Redesenha a tela a cada passagem pelo laço
        gf.update_screen(ai_settings, screen, ship)

        # Deixa a tela mais recente visível
        pygame.display.flip()   

run_game()
