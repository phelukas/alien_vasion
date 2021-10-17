
class GameStatus():
    """Armazena dados estatísticos da Invação Alienígena."""

    def __init__(self, ai_settings):
        """Inicializa os dados estatísticos"""

        self.ai_settings = ai_settings
        self.reset_stats()

        # Inicia o jog em um estado inativo
        self.game_active = False

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""

        self.ships_left = self.ai_settings.ship_limit
        
