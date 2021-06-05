import pygame
from menu import Menu
from sett import Constant

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
            self.game.draw_text("Rules of Breakout Game", 35, Constant.screen_width/2, Constant.screen_height/2 -100)
            self.game.draw_text("The aim of the game is to get the best score ", 25, Constant.screen_width/2, Constant.screen_height/2)
            self.game.draw_text("by breaking all of the bricks",25, Constant.screen_width/2, Constant.screen_height/2 + 25)
            self.game.draw_text("There are following rules:",20, Constant.screen_width/2, Constant.screen_height/2 + 100)
            self.game.draw_text("1) Paddle moves on the left by clicking <left_arrow>", 12, Constant.screen_width/2, Constant.screen_height/2 +130)
            self.game.draw_text("and on the right <right_arrow>,", 12, Constant.screen_width/2, Constant.screen_height/2 +150)
            self.game.draw_text("2) For breaking 1 brick you get +10 score,", 12, Constant.screen_width/2, Constant.screen_height/2 +170)
            self.game.draw_text("3) If the ball falls down the screen, you lose 1 life,", 12, Constant.screen_width/2, Constant.screen_height/2 +190)
            self.game.draw_text("Press <Backspace> to back to the main menu", 10, Constant.screen_width/2, Constant.screen_height/2 +250)
            self.blit_screen()

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
            self.game.draw_text("Credits", 40, Constant.screen_width/2, Constant.screen_height/2 -100)
            self.game.draw_text("Created by:", 30, Constant.screen_width/2, Constant.screen_height/2 + 10)
            self.game.draw_text("Magdalena Szymkowiak", 20, Constant.screen_width/2, Constant.screen_height/2 +60)
            self.game.draw_text("Press <Backspace> to back to the main menu", 10, Constant.screen_width/2, Constant.screen_height/2 +200)
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
class FailingMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game)

