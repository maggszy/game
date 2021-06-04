import pygame
from sett import Constant
from random import randint

#do sth not to let the ball go straight to the wall

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = Constant.screen_width / 2
        self.y_pos = Constant.screen_height / 2
        self.image = pygame.image.load("img/ballBlue.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = [randint(2,4), randint(-4,4)]
        self.rect.center = (self.x_pos, self.y_pos)

        self.sound = pygame.mixer.Sound('sound/bounce_sound.wav')
        self.sound.set_volume(10)


    def update(self):
        if self.x_pos < 11 or self.x_pos > Constant.screen_width -11:
            self.speed[0] =- self.speed[0]
        if self.y_pos < 11:
            self.speed[1] =- self.speed[1]
        if self.speed[0]== 0:
            self.speed[0] += 4
        if self.speed[1] == 0:
            self.speed[1] +=4
        self.x_pos += self.speed[0]
        self.y_pos += self.speed[1]

        self.rect.center = (self.x_pos, self.y_pos)

    def reset(self):
        self.speed = [randint(2,4), randint(-4,4)]
        self.x_pos = Constant.screen_width / 2
        self.y_pos = Constant.screen_height / 2
        self.rect.center = (self.x_pos, self.y_pos)

    def collision_paddle(self,paddle):
        if self.rect.colliderect(paddle.rect):
            if abs(self.rect.bottom - paddle.rect.top) < Constant.collision_treshold and self.speed[1] >0:
                self.speed[1] = -self.speed[1]
                self.speed[0] += paddle.direction
                self.sound.play(0)
                if self.speed[0] > Constant.ball_maxspeed:
                    self.speed[0] = Constant.ball_maxspeed
                if self.speed[0] < -Constant.ball_maxspeed:
                    self.speed[0] = Constant.ball_maxspeed
            else:
                self.speed[0] *= -1 
                self.sound.play(0)


    def off_screen(self):
        return self.y_pos > Constant.screen_height

    def bounce(self):
        self.sound.play(0)
        self.speed[0] = -self.speed[0]
        self.speed[1] = randint(-4,4)
