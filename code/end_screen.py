import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT

class EndScreen:
    def __init__(self, window):
        self.window = window
        self.font_big = pygame.font.SysFont("Arial", 48)
        self.font_small = pygame.font.SysFont("Arial", 24)

    def run(self):
        clock = pygame.time.Clock()
        timer = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            timer += 1
            if timer > 180:  # 3 segundos
                return "menu"

            self.window.fill((0, 0, 0))

            text1 = self.font_big.render("Parabéns!", True, (255, 255, 255))
            text2 = self.font_small.render("Você terminou o Level 1!", True, (255, 255, 255))

            self.window.blit(text1, (WIN_WIDTH // 2 - text1.get_width() // 2, 180))
            self.window.blit(text2, (WIN_WIDTH // 2 - text2.get_width() // 2, 250))

            pygame.display.update()
            clock.tick(60)
