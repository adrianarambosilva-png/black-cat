#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.level import Level

class Level2(Level):
    def __init__(self, window):
        super().__init__(window, "Level2")
        # placeholder: fundo simples
        self.bg = pygame.Surface((600, 480))
        self.bg.fill((30, 30, 60))

    def run_one_frame(self):
        # apenas desenha fundo por enquanto
        self.window.blit(self.bg, (0,0))
