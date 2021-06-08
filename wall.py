import pygame
from sett import Constant

bricks = [
    "img/greenrect.png",
    "img/redrect.png",
    "img/purplerect.png",
    "img/greyrect.png",
    "img/yellowrect.png"
]

class Wall:
    """
    Class that build Wall of bricks 
    """
    def __init__(self, all_sprites):
        """
        Initilize needed variable
        """
        self.all_sprites = all_sprites
        self.all_bricks = pygame.sprite.Group()
        self.score = 0  

        for row in range(Constant.brick_rows):
            for col in range(Constant.brick_cols):
                brick = Brick(row, col)
                self.all_sprites.add(brick)
                self.all_bricks.add(brick)

    def check_collison(self,ball):
        """
        Check collision between bricks and ball
        """
        self.collision_list = pygame.sprite.spritecollide(ball, self.all_bricks, False)
        for brick in self.collision_list:
            ball.bounce()
            brick.kill()
            self.score += 10

    def update(self):
        """
        Update the wall
        """
        for row in range(Constant.brick_rows):
            for col in range(Constant.brick_cols):
                brick = Brick(row, col)
                self.all_sprites.add(brick) 
                self.all_bricks.add(brick)   

class Brick(pygame.sprite.Sprite):
    """
    Class that build the wall
    """
    def __init__(self,row,col):
        super().__init__()
        self.x_pos = Constant.brick_start + (col *64) + 14
        self.y_pos = Constant.brick_start + (row * 32) + 16
        self.image = pygame.image.load(bricks[row])
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)