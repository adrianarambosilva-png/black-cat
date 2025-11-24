#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
import os

from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, C_WHITE

print("Procurando:", os.getcwd())
print("existe?", os.path.exists('./asset/menubd.png'))

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('asset/menubd.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Enter para sair do menu
                        running = False

            pygame.mixer_music.load('./asset/menumusic.wav')
            pygame.mixer_music.play(-1)
            while True:
                self.window.blit(self.surf, self.rect)
                self.menu_text(50, "Black Cat", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))

                for i in range(len(MENU_OPTION)):
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))

                pygame.display.flip()

                # Check for all events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
