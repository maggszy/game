import pygame
import sys
from sett import Constant
from paddle import Paddle
from ball import Ball
from wall import Wall
#do sth with the speed
# and repeat the screen after breaking whole wall 
# to show game over with the background

class Breakout:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Breakout!")
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

        self.failing_sound = pygame.mixer.Sound('sound/game_over.wav')
        self.failing_sound.set_volume(10)

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
        if keys[pygame.K_ESCAPE]:
            sys.exit()

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
            self.failing_sound.play(0)
            gameover = self.font.render("Game Over!", 1, pygame.Color("white"))
            self.screen.blit(gameover,(Constant.screen_width/2 - 75,Constant.screen_height/2))
            #write what to do next
        else:
            self.all_sprites.draw(self.screen)

            msg = self.font.render("Lives: {0}".format(self.paddle.lives),1,pygame.Color("white"))
            self.screen.blit(msg,(15,15))

            score = self.font.render("Score:{0}".format(self.wall.score), 1,pygame.Color("white"))
            self.screen.blit(score,(Constant.screen_width - 100 ,15))
            #scoretext = pygame.font.Font(None,40).render(str(score), True, (0,255,255), bgcolour)
            #scoretextrect = scoretext.get_rect()