import pygame

class Parallax:
    def __init__(self):
        self.bg_back = pygame.image.load("asset/ceufase1.png")
        self.bg_mid = pygame.image.load("asset/luaestrelas.png")
        self.bg_front = pygame.image.load("asset/nuvensfase1.png")

    def draw(self, window, camera_x):
        # Fundo mais lento (céu)
        window.blit(self.bg_back, (-camera_x * 0.1, 0))

        # Camada média (lua e estrelas)
        window.blit(self.bg_mid, (-camera_x * 0.3, 0))

        # Camada frontal (nuvens)
        window.blit(self.bg_front, (-camera_x * 0.6, 0))
