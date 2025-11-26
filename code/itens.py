import pygame

class Item:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.rect = pygame.Rect(x, y, 32, 32)

    def update(self, player_rect):
        if self.rect.colliderect(player_rect):
            return True
        return False

    def draw(self, window, cam_x, cam_y):
        # centralizar sprite dentro do tile
        img = self.img
        w, h = img.get_width(), img.get_height()

        draw_x = self.x - cam_x + (32 - w) // 2
        draw_y = self.y - cam_y + (32 - h)

        window.blit(img, (draw_x, draw_y))
