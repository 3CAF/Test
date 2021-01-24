import pygame as pg

pg.init()
from pygame.locals import (
    K_w,
    K_a,
    K_s,
    K_d,
    K_ESCAPE,
    QUIT,
    KEYDOWN
)

running_game = True

screen_width = 1920
screen_height = 1080

clock = pg.time.Clock()


class Ground(pg.sprite.Sprite):
    def __init__(self):
        super(Ground, self).__init__()
        self.surf = pg.Surface((screen_width, screen_height / 3))
        self.surf.fill((132, 192, 17))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (0, 2 * screen_height / 3)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.Surface((60, 100))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.bottomleft = (screen_width / 2, screen_height * 2 / 3)

    def update(self, pk):
        if pk[K_w] and pg.sprite.spritecollideany(player, ground_sprite):
            self.rect.move_ip(0, -200)
        if pk[K_a]:
            self.rect.move_ip(-5, 0)
        if pk[K_s]:
            self.rect.move_ip(0, 0)
        if pk[K_d]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

        if not pg.sprite.spritecollideany(player, ground_sprite):
            self.rect.move_ip(0, 5)
        else:
            self.rect.move_ip(0, 0)


screen = pg.display.set_mode([screen_width, screen_height])
ground = Ground()
player = Player()

ground_sprite = pg.sprite.Group()
player_sprite = pg.sprite.Group()
all_sprites = pg.sprite.Group()
ground_sprite.add(ground)
player_sprite.add(player)
all_sprites.add(ground_sprite)
all_sprites.add(player_sprite)

playercc = 0

while running_game:

    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running_game = False

        elif event.type == pg.QUIT:
            running_game = False

    screen.fill((135, 206, 250))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pressed_keys = pg.key.get_pressed()
    player.update(pressed_keys)

    pg.display.flip()
    clock.tick(90)
