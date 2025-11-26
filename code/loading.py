import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT

def show_loading(window):
    font_big = pygame.font.SysFont("Arial", 36)
    font_small = pygame.font.SysFont("Arial", 20)

    loading_bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    loading_bg.fill((10, 10, 30))

    title = font_big.render("Level 1", True, (255, 255, 255))
    subtitle = font_small.render("Carregando...", True, (200, 200, 200))

    clock = pygame.time.Clock()
    timer = 0

    while timer < 45:      # ~0.75 segundos
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.blit(loading_bg, (0, 0))
        window.blit(title, (WIN_WIDTH//2 - title.get_width()//2, 180))
        window.blit(subtitle, (WIN_WIDTH//2 - subtitle.get_width()//2, 240))

        pygame.display.update()
        timer += 1
        clock.tick(60)
