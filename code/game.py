import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.menu import Menu
from code.level1 import Level1
from code.game_over import GameOverScreen
from code.end_screen import EndScreen
from code.loading import show_loading


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Black Cat")

    def run(self):
        while True:
            menu = Menu(self.window)
            result = menu.run()

            if result == MENU_OPTION[0]:  # NOVO JOGO
                show_loading(self.window)  # tela de carregamento

                outcome = self.run_level()

                if outcome == "gameover":
                    GameOverScreen(self.window).run()
                elif outcome == "end":
                    EndScreen(self.window).run()

            elif result == MENU_OPTION[2]:  # EXIT
                pygame.quit()
                quit()

    def run_level(self):
        level = Level1(self.window)
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            level.update()
            level.draw()
            pygame.display.update()
            clock.tick(60)

            if level.game_over:
                return "gameover"

            if level.completed:
                return "end"
