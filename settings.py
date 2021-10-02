
class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alien"""

    def __init__(self):
        """Inicializa as configurações do jogo"""
        # Configurações de tela
        self.screen_width = 1300
        self.screen_height = 690
        self.bg_color = (230, 230, 230)
        
        # Configuração da espaçonave
        self.ship_speed_factor = 1.5
        