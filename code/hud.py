import pygame

class HUD:
    def __init__(self):
        self.heart = pygame.image.load("asset/coracao.png").convert_alpha()
        self.peixe = pygame.image.load("asset/peixe.png").convert_alpha()

    def draw(self, window, lives, collected, total):
        font = pygame.font.SysFont("Arial", 26)

        # vidas
        for i in range(lives):
            window.blit(self.heart, (10 + i * 40, 10))

        # contador de peixes com ícone
        window.blit(self.peixe, (10, 55))
        txt = font.render(f"{collected}/{total}", True, (255, 255, 255))
        window.blit(txt, (50, 55))
