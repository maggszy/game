import pygame
from sett import Constant

bricks = [
    "img/bluerect.png",
    "img/redrect.png",
    "img/purplerect.png",
    "img/greenrect.png",
    "img/yellowrect.png"
]

class Wall:
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.all_bricks = pygame.sprite.Group()

        for row in range(Constant.brick_rows):
            for col in range(Constant.brick_cols):
                brick = Brick(row, col)
                self.all_sprites.add(brick)
                self.all_bricks.add(brick)

    def check_collison(self,ball):
        collision_list = pygame.sprite.spritecollide(ball, self.all_bricks, False)
        for brick in collision_list:
            ball.bounce()
            brick.kill()

class Brick(pygame.sprite.Sprite):
    def __init__(self,row,col):
        super().__init__()
        self.x_pos = Constant.brick_start + (col *64) + 16
        self.y_pos = Constant.brick_start + (row * 32) + 16
        self.image = pygame.image.load(bricks[row])
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)

