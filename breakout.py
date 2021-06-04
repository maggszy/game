import pygame
import sys
from sett import Constant
from paddle import Paddle
from ball import Ball
from wall import Wall
#it will go to the breakout.py 

class Breakout:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constant.screen_width,Constant.screen_height))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color("black")
        self.font = pygame.font.Font("kenney_future.ttf", 16)
        self.game_over = False


        self.paddle = Paddle()
        self.ball = Ball()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.paddle, self.ball)

        self.wall = Wall(self.all_sprites)

    def reset(self):
        self.game_over = False
        self.paddle = Paddle()
        self.ball = Ball()

        self.all_sprites.empty()
        self.all_sprites.add(self.paddle,self.ball)
        self.wall = Wall(self.all_sprites)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move_left()
        if keys[pygame.K_RIGHT]:
            self.paddle.move_right()
        if self.game_over and keys[pygame.K_SPACE]:
            self.reset()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        if self.ball.off_screen():
            self.paddle.lose_life()
            if self.paddle.lives <= 0:
                self.game_over = True
            self.ball.reset()
        self.ball.collision_paddle(self.paddle)
        self.wall.check_collison(self.ball)
        self.all_sprites.update()
        pygame.display.update()
        self.clock.tick(120)

    def draw(self):
        self.screen.fill(self.bg_color)

        if self.game_over:
            msg = self.font.render("Game Over!", 1, pygame.Color("white"))
            self.screen.blit(msg,(Constant.screen_width/2 - 75,Constant.screen_height/2))
        else:
            self.all_sprites.draw(self.screen)

            msg = self.font.render("Lives: {0}".format(self.paddle.lives),1,pygame.Color("white"))
            self.screen.blit(msg,(15,15))
