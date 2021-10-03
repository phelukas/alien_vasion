from pygame.sprite import Sprite

import pygame

class Alien(Sprite):
    """Uma classe que representa um único alienígina da frota"""

    def __init__(self, ai_settings, screen):
        """Inicializa o alienígena e define sua posição inicial"""

        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do alienígena e define seu atributo rect 
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada nova alienígina prox. à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígina 
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alienígina em sua posição atual"""

        self.screen.blit(self.image, self.rect)
