import pygame

GRAVITY = 0.6
JUMP_FORCE = -12
MOVE_SPEED = 4


class Player:
    def __init__(self, x, y):
        # posição
        self.rect = pygame.Rect(x, y, 28, 32)

        # guardar spawn
        self.spawn_x = x
        self.spawn_y = y

        # velocidade vertical
        self.vel_y = 0

        # estado do chão
        self.on_ground = False

        # animações
        self.img_idle = pygame.image.load("asset/Gatoparado.png").convert_alpha()
        self.img_walk1 = pygame.image.load("asset/Gatoandando.png").convert_alpha()
        self.img_walk2 = pygame.image.load("asset/Gatoandando2.png").convert_alpha()

        self.walk_frames = [self.img_walk1, self.img_walk2]
        self.frame_index = 0
        self.frame_timer = 0

        self.facing = 1  # 1 = direita, -1 = esquerda

    # ---------------------------------------------------------
    # RESPAWN
    # ---------------------------------------------------------
    def respawn(self):
        self.rect.x = self.spawn_x
        self.rect.y = self.spawn_y
        self.vel_y = 0

    # ---------------------------------------------------------
    # ATUALIZAÇÃO
    # ---------------------------------------------------------
    def update(self, plataformas, offset_y=0):
        keys = pygame.key.get_pressed()

        dx = 0

        # andar
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -MOVE_SPEED
            self.facing = -1

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = MOVE_SPEED
            self.facing = 1

        # pular
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y = JUMP_FORCE

        # aplicar gravidade
        self.vel_y += GRAVITY
        dy = self.vel_y

        # ----- colisão corrigida com offset vertical -----
        plataformas_ajustadas = [p.move(0, offset_y) for p in plataformas]

        # mover horizontal com colisão
        self.rect.x += dx
        for p in plataformas_ajustadas:
            if self.rect.colliderect(p):
                if dx > 0:
                    self.rect.right = p.left
                elif dx < 0:
                    self.rect.left = p.right

        # mover vertical com colisão
        self.on_ground = False
        self.rect.y += dy

        for p in plataformas_ajustadas:
            if self.rect.colliderect(p):
                if dy > 0:
                    self.rect.bottom = p.top
                    self.vel_y = 0
                    self.on_ground = True
                elif dy < 0:
                    self.rect.top = p.bottom
                    self.vel_y = 0

        # animação de caminhada
        if dx != 0:
            self.frame_timer += 1
            if self.frame_timer >= 12:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.walk_frames)
        else:
            self.frame_index = 0

    # ---------------------------------------------------------
    # DESENHO
    # ---------------------------------------------------------
    def draw(self, window, cam_x, cam_y):
        if self.rect is None:
            return

        # escolher frame
        img = self.img_idle
        if not self.on_ground:
            img = self.img_walk1
        else:
            if self.frame_index == 0:
                img = self.img_walk1
            else:
                img = self.img_walk2

        # inverter se estiver virado pra esquerda
        if self.facing == -1:
            img = pygame.transform.flip(img, True, False)

        window.blit(img, (self.rect.x - cam_x, self.rect.y - cam_y))
