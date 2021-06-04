import pygame
from sett import Constant

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/paddleRed.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.y_pos = Constant.screen_height - 50 #paddle will be 50px up the bottom of screen
        self.x_pos = Constant.screen_width / 2
        self.rect.center = (self.x_pos, self.y_pos)
        self.direcition = 0 #direction of the paddle
        self.lives = Constant.start_lives
    
    def update(self):
        if self.x_pos < 52: #half of the x size of paddle
            self.x_pos = 52
        if self.x_pos > (Constant.screen_width - 52):
            self.x_pos = Constant.screen_width - 52
        self.rect.center = (self.x_pos, self.y_pos)

    def lose_life(self):
        self.lives -=1

    def reset(self):
        self.lives = Constant.start_lives

    def move_left(self):
        self.x_pos -=Constant.paddle_speed
        self.direction = -1 #controlling speed

    def move_right(self):
        self.x_pos += Constant.paddle_speed
        self.direction = 1 
           