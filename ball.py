import pygame
from sett import Constant
from random import randint

class Ball(pygame.sprite.Sprite):
    """
    Class contains methods made on ball object
    """
    def __init__(self):
        super().__init__()
        self.x_pos = Constant.screen_width / 2
        self.y_pos = Constant.screen_height / 2
        self.image = pygame.image.load("img/ballGrey.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = [randint(-4,4), randint(2,4)]
        self.rect.center = (self.x_pos, self.y_pos)

        self.sound = pygame.mixer.Sound('sound/bounce_sound.wav')
        self.sound.set_volume(10)

    def update(self):
        """
        Method that updates speed of ball
        """
        if self.x_pos < 11 or self.x_pos > Constant.screen_width -11:
            self.speed[0] =- self.speed[0]
        if self.y_pos < 11:
            self.speed[1] =- self.speed[1]
        if self.speed[0]== 0 or self.speed[0]== 1:
            self.speed[0] += 4
        if self.speed[1] == 0:
            self.speed[1] +=4
        self.x_pos += self.speed[0]
        self.y_pos += self.speed[1]

        self.rect.center = (self.x_pos, self.y_pos)

    def reset(self):
        """
        Method used while putting ball again in the screen
        """
        self.speed = [randint(2,4), randint(2,4)]
        self.x_pos = Constant.screen_width / 2
        self.y_pos = Constant.screen_height / 2
        self.rect.center = (self.x_pos, self.y_pos)

    def collision_paddle(self,paddle):
        """
        Checking and reacting on the collision ball with paddle
        """
        if self.rect.colliderect(paddle.rect):
            if abs(self.rect.bottom - paddle.rect.top) < Constant.collision_treshold and self.speed[1] >0:
                self.speed[1] = -self.speed[1]
                self.speed[0] += paddle.way
                self.sound.play(0)
                if self.speed[0] > Constant.ball_maxspeed:
                    self.speed[0] = Constant.ball_maxspeed
                if self.speed[0] < -Constant.ball_maxspeed:
                    self.speed[0] = Constant.ball_maxspeed
            else:
                self.speed[0] *= -1 
                self.sound.play(0)

    def off_screen(self):
        """
        Checking if ball if of the screen
        """
        return self.y_pos > Constant.screen_height

    def bounce(self):
        """
        Bouncing of the broken brick
        """
        self.sound.play(0)
        self.speed[0] = -self.speed[0]
        self.speed[1] = randint(2,4)
