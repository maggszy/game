import pygame
from sett import Constant

class Menu:
    def __init__(self,game):
        self.game = game
        self.half_w, self.half_h = Constant.screen_width/2, Constant.screen_height/2
        self.display_run = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text("*",20,self.cursor_rect.x - 10,self.cursor_rect.y, pygame.Color("red"))

    def blit_screen(self):
        self.game.screen.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self,game)
        self.state = "Start"
        self.startx, self.starty = self.half_w, self.half_h
        self.rulesx, self.rulesy = self.half_w, self.half_h +30
        self.scoresx, self.scoresy = self.half_w, self.half_h +60
        self.creditsx, self.creditsy = self.half_w, self.half_h + 90
        self.quitx, self.quity = self.half_w, self.half_h + 120
        self.msgx, self.msgy = self.half_w, self.half_h + 270
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def show_menu(self):
        self.display_run = True
        while self.display_run:
            self.game.handle_events()
            self.check_button()
            self.game.display.blit(self.game.bg_img4, (0,0))
            self.game.draw_text("Main Menu", 40, self.half_w, self.half_h -100)
            self.game.draw_text("Start Game", 25, self.startx, self.starty)
            self.game.draw_text("Rules", 25, self.rulesx, self.rulesy)
            self.game.draw_text("High Scores", 25, self.scoresx, self.scoresy)
            self.game.draw_text("Credits", 25, self.creditsx, self.creditsy)
            self.game.draw_text("Quit", 25, self.quitx, self.quity)
            self.game.draw_text("Press <up_arrow> to move cursor up and <down_arrow> to move it down", 10, self.msgx, self.msgy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            self.game.menu_sound.play(0)
            if self.state == "Start":
                self.cursor_rect.midtop = (self.rulesx + self.offset, self.rulesy)
                self.state = "Rules"
            elif self.state == "Rules":
                self.cursor_rect.midtop = (self.scoresx + self.offset, self.scoresy)
                self.state = "Scores"
            elif self.state == "Scores":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quitt"
            elif self.state == "Quitt":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
        if self.game.UP_KEY:
            self.game.menu_sound.play(0)
            if self.state == "Start":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quitt"
            elif self.state == "Rules":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == "Scores":
                self.cursor_rect.midtop = (self.rulesx + self.offset, self.rulesy)
                self.state = "Rules"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.scoresx + self.offset, self.scoresy)
                self.state = "Scores"
            elif self.state == "Quitt":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
        
    def check_button(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Rules":
                self.game.current_menu = self.game.rules
            elif self.state == "Scores":
                self.game.current_menu = self.game.scores
            elif self.state == "Credits":
                self.game.current_menu = self.game.credits
            elif self.state == "Quitt":
                self.game.current_menu = self.game.quiit
            self.display_run = False