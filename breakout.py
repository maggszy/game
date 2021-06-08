import pygame
import sys
from sett import Constant
from paddle import Paddle
from ball import Ball
from wall import Wall
from menu import MainMenu
from othermenu import *
import json 

class Breakout:
    """
    The main class connecting the whole game
    """
    def __init__(self):
        """
        Initialize needed variables
        """
        pygame.init()
        pygame.display.set_caption("Breakout!")
        self.running, self.playing = True, False
        self.width, self.height = 800, 600
        self.display = pygame.Surface((self.width,self.height))
        self.screen = pygame.display.set_mode((Constant.screen_width,Constant.screen_height))
        self.UP_KEY= Constant.UP_KEY 
        self.DOWN_KEY=Constant.DOWN_KEY  
        self.START_KEY= Constant.START_KEY 
        self.BACK_KEY = Constant.BACK_KEY 
        self.final_score = 0
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

        self.menu_sound = pygame.mixer.Sound('sound/menu2.wav')
        self.menu_sound.set_volume(10)

        icon = pygame.image.load("img/icon.png")
        pygame.display.set_icon(icon)

        self.left = pygame.image.load("img/left.png").convert_alpha()
        self.left = pygame.transform.scale(self.left,(40,40))
        self.right = pygame.image.load("img/right.png").convert_alpha()
        self.right = pygame.transform.scale(self.right,(40,40))

    def reset(self):
        """
        Reset game
        """
        self.game_over = False
        self.paddle = Paddle()
        self.ball = Ball()

        self.all_sprites.empty()
        self.all_sprites.add(self.paddle,self.ball)
        self.wall = Wall(self.all_sprites)

    def breakout_loop(self):
        """
        Method that runs the breakout
        """
        while self.playing:
            self.handle_events()
            self.update()
            if self.game_over:
                self.current_menu = self.fail_menu
                self.playing = False
                self.reset()
            self.draw()

    def game_loop(self):
        """
        Run the whole game including menu
        """
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
        """
        Check button and react adequately
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move_left()
        if keys[pygame.K_RIGHT]:
            self.paddle.move_right()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
        """
        Reset keys to the starting state
        """
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False


    def update(self):
        """
        Update the game
        """
        if self.ball.off_screen():
            self.paddle.lose_life()
            if self.paddle.lives <= 0:
                self.saving_score()
                self.list_of_scores()
                self.game_over = True
                self.failing_sound.play(0)
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
        """
        Display text on the screen
        """
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

        
    
    def saving_score(self):
        """
        Save gained scores
        """
        with open(Constant.this_score, "r+") as f:
            f.truncate(0)
            this_score = self.final_score
            f.write(this_score)

    def list_of_scores(self):
        """
        Check list of high scores with gained score and put the fresh one in the right place
        """
        with open(Constant.this_score, "r") as f:
            final= f.read()
            final = int(final)
        with open(Constant.list_scores, "r") as li:
            points_file = json.load(li)
            points = points_file['HighScores']

            with open(Constant.list_scores,"w") as files:

                if len(points) == 5:
                    if points[0] < final:
                        for i in range(len(points)-1,0,-1):
                            points[i] = points[i-1]
                        points[0] = final
                        json.dump(points_file,files)
                    elif points[0] > final:
                        if points[1] < final:
                            for i in range(len(points)-1,1,-1):
                                points[i] = points[i-1]
                            points[1] = final
                            json.dump(points_file,files)
                        elif points[1] > final:
                            if points[2] < final:
                                for i in range(len(points)-1,2,-1):
                                    points[i] = points[i-1]
                                points[2] = final
                                json.dump(points_file,files)
                            elif points[2] > final:
                                if points[3] < final:
                                    for i in range(len(points)-1,3,-1):
                                        points[i] = points[i-1]
                                    points[3] = final
                                    json.dump(points_file,files)
                                elif points[3] > final:
                                    if points[4] < final:
                                        points[4] = final
                                        json.dump(points_file,files)
                                    else:
                                        json.dump(points_file,files)
                                else:
                                    json.dump(points_file,files)
                            else:
                                json.dump(points_file,files)
                        else:
                            json.dump(points_file,files)
                    else:
                        json.dump(points_file,files)

    def draw(self):
        """
        Draw all the sprites and Lives and Score on the screen
        """
        self.screen.blit(self.bg_img4, (0,0))
        self.all_sprites.draw(self.screen)
        self.final_score = "{0}".format(self.wall.score)
        msg = self.font.render("Lives: {0}".format(self.paddle.lives),1,pygame.Color("white"))
        self.screen.blit(msg,(15,15))
        score = self.font.render("Score:" + self.final_score, 1,pygame.Color("white"))
        self.screen.blit(score,(Constant.screen_width - 150 ,15))