import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT

class GameOverScreen:
    def __init__(self, window):
        self.window = window
        self.font_big = pygame.font.SysFont("Arial", 52)
        self.font_small = pygame.font.SysFont("Arial", 24)

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "menu"  # volta ao menu

            # fundo
            self.window.fill((0, 0, 0))

            # textos
            text1 = self.font_big.render("GAME OVER", True, (255, 80, 80))
            text2 = self.font_small.render("Aperte ENTER para voltar ao menu", True, (255, 255, 255))

            self.window.blit(text1, (WIN_WIDTH // 2 - text1.get_width() // 2, 180))
            self.window.blit(text2, (WIN_WIDTH // 2 - text2.get_width() // 2, 270))

            pygame.display.update()
            clock.tick(60)
