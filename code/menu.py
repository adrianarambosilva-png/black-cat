#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import os

from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, WIN_HEIGHT, C_BLACK, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('asset/menubd.png').convert()
        self.rect = self.surf.get_rect(left=0, top=0)

        # Música do menu
        pygame.mixer.music.load('asset/menumusic.wav')
        pygame.mixer.music.play(-1)

    def run(self):
        menu_option = 0
        running = True

        while running:

            # EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)

                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]  # <-- retorna escolha

            # ===== DESENHO =====
            self.window.blit(self.surf, self.rect)

            # Título
            self.menu_text(50, "Black Cat", C_BLACK, (WIN_WIDTH / 2, 70))

            # Opções do menu
            for i in range(len(MENU_OPTION)):
                cor = C_YELLOW if i == menu_option else C_WHITE
                self.menu_text(25, MENU_OPTION[i], cor, (WIN_WIDTH / 2, 200 + 45 * i))

            # --- COMANDOS NO CANTO INFERIOR DIREITO ---
            self.menu_text(18, "Espaço = pular", C_WHITE, (WIN_WIDTH - 120, WIN_HEIGHT - 60))
            self.menu_text(18, "Setas = mover", C_WHITE, (WIN_WIDTH - 120, WIN_HEIGHT - 30))

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, pos: tuple):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=pos)
        self.window.blit(text_surf, text_rect)
