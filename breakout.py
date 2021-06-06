import pygame
import sys
from sett import Constant
from paddle import Paddle
from ball import Ball
from wall import Wall
from menu import MainMenu
from othermenu import *
#do sth with the speed
# and repeat the screen after breaking whole wall  :DDDD DONEEEE
#return some messages with the "GAME OVER!" 
# (like:score, buttons to go to the menu,clues how to restart or guit)

class Breakout:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Breakout!")
        self.running, self.playing = True, False
        self.width, self.height = 800, 600
        self.display = pygame.Surface((self.width,self.height))
        self.screen = pygame.display.set_mode((Constant.screen_width,Constant.screen_height))
        self.UP_KEY= Constant.UP_KEY #false
        self.DOWN_KEY=Constant.DOWN_KEY  #false
        self.START_KEY= Constant.START_KEY #false
        self.BACK_KEY = Constant.BACK_KEY #false
        self.clock = pygame.time.Clock()

        self.main_menu = MainMenu(self)
        self.rules = RulesMenu(self)
        self.credits = CreditsMenu(self)
        self.scores = ScoresMenu(self)
        self.quiit = Quiit(self)
        self.fail_menu = GameOverMenu(self)
        self.current_menu = self.main_menu

        self.bg_img4 =  pygame.image.load("img/galaxx3.png").convert_alpha()
        self.bg_color = pygame.Color("black")
        self.font = pygame.font.Font("kenney_future.ttf", 16)
        self.font_name = "kenney_future.ttf"
        self.game_over = False


        self.paddle = Paddle()
        self.ball = Ball()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.paddle, self.ball)

        self.wall = Wall(self.all_sprites)

        self.failing_sound = pygame.mixer.Sound('sound/game_over.wav')
        self.failing_sound.set_volume(10)

        icon = pygame.image.load("img/icon.png")
        pygame.display.set_icon(icon)


    #do not need change 
    def reset(self):
        self.game_over = False
        self.paddle = Paddle()
        self.ball = Ball()

        self.all_sprites.empty()
        self.all_sprites.add(self.paddle,self.ball)
        self.wall = Wall(self.all_sprites)

    def breakout_loop(self):
        while self.playing:
            self.handle_events()
            self.update()
            if self.game_over:
                self.current_menu = self.fail_menu
                self.playing = False
                self.reset()
            self.draw()

    def game_loop(self):
        while self.playing:
            self.handle_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.bg_color)
            self.breakout_loop()
            self.screen.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move_left()
        if keys[pygame.K_RIGHT]:
            self.paddle.move_right()
        #if self.game_over and keys[pygame.K_SPACE]:
         #   self.reset()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                #sys.exit()
                self.running, self.playing = False, False
                self.current_menu.display_run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False


    def update(self):
        if self.ball.off_screen():
            self.paddle.lose_life()
            if self.paddle.lives <= 0:
                self.game_over = True
            self.ball.reset()
        self.ball.collision_paddle(self.paddle)
        self.wall.check_collison(self.ball)
        if not self.wall.all_bricks:
            self.wall.update()
            self.ball.reset()
        self.all_sprites.update()
        pygame.display.update()
        self.clock.tick(120)

    def draw_text(self, text, size, x, y ,color=pygame.Color("white")):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
    


    def draw(self):
        self.screen.blit(self.bg_img4, (0,0))

        #if self.game_over:
         #   self.failing_sound.play(0)
          #  #self.current_menu = self.main_menu
           # gameover = self.font.render("Game Over!", 1, pygame.Color("white"))
            #self.screen.blit(gameover,(Constant.screen_width/2 - 75,Constant.screen_height/2))
            #self.screen.blit(score,(Constant.screen_width/2 ,500))
            
            # display your final score
        #else:
        self.all_sprites.draw(self.screen)

        msg = self.font.render("Lives: {0}".format(self.paddle.lives),1,pygame.Color("white"))
        self.screen.blit(msg,(15,15))
        score = self.font.render("Score:{0}".format(self.wall.score), 1,pygame.Color("white"))
        self.screen.blit(score,(Constant.screen_width - 150 ,15))