import pygame
from pytmx.util_pygame import load_pygame
from code.player import Player
from code.itens import Item
from code.hud import HUD
from code.const import WIN_WIDTH, WIN_HEIGHT


TILE = 32


class Level1:
    def __init__(self, window):
        self.window = window

        # carregar TMX
        self.tmx = load_pygame("asset/level1.tmx")

        self.width = self.tmx.width * TILE
        self.height = self.tmx.height * TILE

        # música do level
        try:
            pygame.mixer.music.load("asset/level1.wav")
            pygame.mixer.music.play(-1)
        except:
            print("⚠ Não foi possível carregar level1.wav")

        # fundo
        try:
            self.background = pygame.image.load("asset/noite.png").convert()
        except:
            self.background = None

        # HUD
        self.hud = HUD()

        # listas
        self.platforms = []
        self.peixes = []
        self.lata = None

        # player + estado
        self.player = None
        self.lives = 3
        self.collected = 0
        self.total_peixes = 0

        # controle de estado
        self.completed = False
        self.game_over = False

        # câmera
        self.cam_x = 0
        self.cam_y = 0

        # carregar dados do mapa
        self.load_map()

    # -----------------------------------------------------
    def load_map(self):
        # CAMADA DE TILES
        layer = self.tmx.layers[0]  # "plataformas"

        for y in range(layer.height):
            for x in range(layer.width):
                gid = layer.data[y][x]
                if gid != 0:
                    rect = pygame.Rect(x * TILE, y * TILE, TILE, TILE)
                    self.platforms.append(rect)

        # OBJETOS
        for obj in self.tmx.objects:

            if obj.name == "spawn":
                self.player = Player(obj.x, obj.y)

            elif obj.name == "peixe":
                img = pygame.image.load("asset/peixe.png").convert_alpha()
                self.peixes.append(Item(obj.x, obj.y, img))

            elif obj.name == "lata":
                img = pygame.image.load("asset/lata.png").convert_alpha()
                self.lata = Item(obj.x, obj.y, img)

        self.total_peixes = len(self.peixes)

        if not self.player:
            print("⚠ Spawn não encontrado! Criando fallback.")
            self.player = Player(50, 50)

    # -----------------------------------------------------
    def update(self):
        self.player.update(self.platforms)

        # coletar peixes
        for peixe in self.peixes[:]:
            if peixe.update(self.player.rect):
                self.peixes.remove(peixe)
                self.collected += 1

        # coletar lata (só após pegar todos os peixes)
        if self.collected == self.total_peixes and self.lata:
            if self.lata.update(self.player.rect):
                self.completed = True

        # morte ao cair
        if self.player.rect.y > self.height:
            self.lives -= 1
            self.player.respawn()

            if self.lives <= 0:
                self.game_over = True

        # câmera centrada no player
        self.cam_x = self.player.rect.x - WIN_WIDTH // 2
        self.cam_y = self.player.rect.y - WIN_HEIGHT // 2

        # limitações
        self.cam_x = max(0, min(self.cam_x, self.width - WIN_WIDTH))
        self.cam_y = max(0, min(self.cam_y, self.height - WIN_HEIGHT))

    # -----------------------------------------------------
    def draw(self):
        # fundo
        if self.background:
            self.window.blit(self.background, (0, 0))

        # desenhar tiles
        layer = self.tmx.layers[0]

        for y in range(layer.height):
            for x in range(layer.width):
                gid = layer.data[y][x]
                if gid != 0:
                    img = self.tmx.get_tile_image_by_gid(gid)
                    if img:
                        self.window.blit(
                            img,
                            (x * TILE - self.cam_x, y * TILE - self.cam_y)
                        )

        # itens
        for peixe in self.peixes:
            peixe.draw(self.window, self.cam_x, self.cam_y)

        if self.collected == self.total_peixes and self.lata:
            self.lata.draw(self.window, self.cam_x, self.cam_y)

        # player
        self.player.draw(self.window, self.cam_x, self.cam_y)

        # HUD
        self.hud.draw(self.window, self.lives, self.collected, self.total_peixes)
