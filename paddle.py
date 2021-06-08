import pygame
from sett import Constant

class Paddle(pygame.sprite.Sprite):
    """
    Class containing object paddle and its methods
    """
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/paddleRed.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.y_pos = Constant.screen_height - 50 
        self.x_pos = Constant.screen_width / 2
        self.rect.center = (self.x_pos, self.y_pos)
        self.way = 0
        self.lives = Constant.start_lives
    
    def update(self):
        """
        Update the position of paddle
        """
        if self.x_pos < 52: #half of the x size of paddle
            self.x_pos = 52
        if self.x_pos > (Constant.screen_width - 52):
            self.x_pos = Constant.screen_width - 52
        self.rect.center = (self.x_pos, self.y_pos)

    def lose_life(self):
        """
        Sintraction life after losing
        """
        self.lives -=1

    def reset(self):
        """
        Restet lives
        """
        self.lives = Constant.start_lives

    def move_left(self):
        """
        Move paddle on the left
        """
        self.x_pos -=Constant.paddle_speed
        self.way = -1 #controlling speed

    def move_right(self):
        """
        Move paddle on the right
        """
        self.x_pos += Constant.paddle_speed
        self.way = 1 
           