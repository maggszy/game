import pygame
from menu import Menu
from sett import Constant
import sys

class RulesMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)

    def show_menu(self):
        #add a picture
        self.display_run = True
        while self.display_run:
            self.game.handle_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.current_menu = self.game.main_menu
                self.display_run = False
            #self.game.display.fill(self.game.bg_color)
            self.game.display.blit(self.game.bg_img4, (0,0))
            self.game.draw_text("Rules of Breakout Game", 35, self.half_w, self.half_h -100)
            self.game.draw_text("The aim of the game is to get the best score ", 25, self.half_w, self.half_h)
            self.game.draw_text("by breaking all of the bricks",25, self.half_w, self.half_h + 25)
            self.game.draw_text("There are following rules:",20, self.half_w, self.half_h + 100)
            self.game.draw_text("1) Paddle moves on the left by pressing <left_arrow>", 12, self.half_w, self.half_h +130)
            self.game.draw_text("and on the right <right_arrow>,", 12, self.half_w, self.half_h +150)
            self.game.draw_text("2) For breaking 1 brick you get +10 score,", 12, self.half_w, self.half_h +170)
            self.game.draw_text("3) If the ball falls down the screen, you lose 1 life,", 12, self.half_w, self.half_h +190)
            self.game.draw_text("Press <Backspace> to back to the main menu", 10, self.half_w, self.half_h +250)
            self.blit_screen()

class Quiit(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)
    
    def show_menu(self):
        self.display_run = True
        while self.display_run:
            pygame.quit()
            sys.exit()
        

class CreditsMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)

    def show_menu(self):
        self.display_run = True
        while self.display_run:
            self.game.handle_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.current_menu = self.game.main_menu
                self.display_run = False
            #self.game.display.fill(self.game.bg_color)
            self.game.display.blit(self.game.bg_img4, (0,0))
            self.game.draw_text("Credits", 40, self.half_w, self.half_h -100)
            self.game.draw_text("Created by:", 30, self.half_w, self.half_h + 10)
            self.game.draw_text("Magdalena Szymkowiak", 20, self.half_w, self.half_h +60)
            self.game.draw_text("Press <Backspace> to back to the main menu", 10, self.half_w, self.half_h +250)
            self.game.draw_text("Production date: 2021", 10, 90, Constant.screen_height- 20)
            self.blit_screen()
#needs finisking
class ScoresMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)
    
    def show_menu(self):
        self.display_run = True
        while self.display_run:
            self.game.handle_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.current_menu = self.game.main_menu
                self.display_run = False
            self.game.display.blit(self.game.bg_img4, (0,0))
            self.blit_screen()

#maybe not necessary   
class GameOverMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)
        #self.game.game_over = True
        self.state = "Restart"
        self.game_overx, self.game_overy = self.half_w, self.half_h -100
        self.scorex, self.scorey = self.half_w, self.half_h -50
        self.restartx, self.restarty = self.half_w, self.half_h + 50
        self.main_menux, self.main_menuy = self.half_w, self.half_h + 100
        self.high_scorex, self.high_scorey = self.half_w, self.half_h + 150
        self.quitx, self.quity = self.half_w, self.half_h + 200
        self.cursor_rect.midtop = (self.restartx + self.offset, self.restarty)

    def show_menu(self):
        self.display_run = True
        while self.display_run:
            self.game.handle_events()
            self.check_button()
            #self.game.display.fill(self.game.bg_color)
            self.game.display.blit(self.game.bg_img4, (0,0))
            self.game.draw_text("Game over!!!", 40, self.game_overx, self.game_overy)
            self.game.draw_text("Score: {0}".format(self.game.wall.score), 25,self.scorex, self.scorey, pygame.Color("red"))
            self.game.draw_text("Restart", 25, self.restartx, self.restarty)
            self.game.draw_text("Main Menu", 25, self.main_menux, self.main_menuy)
            self.game.draw_text("High Scores", 25,self.high_scorex, self.high_scorey)
            self.game.draw_text("Quit", 25,self.quitx, self.quity)
            #self.game.draw_text("Press <Space> to restart game", 10, self.half_w, self.half_h +250)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Restart":
                self.cursor_rect.midtop = (self.main_menux + self.offset, self.main_menuy)
                self.state = "Main"
            elif self.state == "Main":
                self.cursor_rect.midtop = (self.high_scorex + self.offset, self.high_scorey)
                self.state = "HighScore"
            elif self.state == "HighScore":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.restartx + self.offset, self.restarty)
                self.state = "Restart"
        if self.game.UP_KEY:
            if self.state == "Restart":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit"
            elif self.state == "Main":
                self.cursor_rect.midtop = (self.restartx + self.offset, self.restarty)
                self.state = "Restart"
            elif self.state == "HighScore":
                self.cursor_rect.midtop = (self.main_menux + self.offset, self.main_menuy)
                self.state = "Main"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.high_scorex + self.offset, self.high_scorey)
                self.state = "HighScore"

    def check_button(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Restart":
                self.game.playing = True
                self.game.reset()
            elif self.state == "Main":
                self.game.current_menu = self.game.main_menu
            elif self.state == "HighScore":
                self.game.current_menu = self.game.scores
            elif self.state == "Quit":
                self.game.current_menu = self.game.quiit
            self.display_run = False

