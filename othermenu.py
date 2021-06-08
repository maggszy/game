import pygame
from menu import Menu
from sett import Constant
import sys
import json

class RulesMenu(Menu):
    """
    Display the view and action after pressing 'Rules' button on the main menu
    """
    def __init__(self,game):
        Menu.__init__(self,game)

    def show_menu(self):
        """
        Display the view of 'Rules' menu 
        """
        self.display_run = True
        while self.display_run:
            self.game.handle_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.current_menu = self.game.main_menu
                self.display_run = False
            self.game.display.blit(self.game.bg_img4, (0,0))
            self.game.draw_text("Rules of Breakout Game", 40, self.half_w, self.half_h -100)
            self.game.draw_text("1) Paddle moves on the left by pressing            ", 20, self.half_w, self.half_h )
            self.game.display.blit(self.game.left,(self.half_w + 260,self.half_h-20))
            self.game.draw_text("and on the right by pressing           ,", 20, self.half_w, self.half_h +40)
            self.game.display.blit(self.game.right,(self.half_w + 170,self.half_h +20))
            self.game.draw_text("2) For breaking 1 brick you get +10 score,", 20, self.half_w, self.half_h +80)
            self.game.draw_text("3) If the ball falls down the screen, you lose 1 life,", 20, self.half_w, self.half_h +120)
            self.game.draw_text("Press <Backspace> to back to the main menu", 10, self.half_w, self.half_h +270)
            self.blit_screen()

class Quiit(Menu):
    """
    Quit the game
    """
    def __init__(self,game):
        Menu.__init__(self,game)
    
    def show_menu(self):
        """
        Quit the game
        """
        self.display_run = True
        while self.display_run:
            pygame.quit()
            sys.exit()
        
class CreditsMenu(Menu):
    """
    Display view o the menu after pressing 'Credits' on the main menu
    """
    def __init__(self,game):
        Menu.__init__(self,game)

    def show_menu(self):
        """
        Display the buttons and the whole view of 'Credits' menu
        """
        self.display_run = True
        while self.display_run:
            self.game.handle_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.current_menu = self.game.main_menu
                self.display_run = False
            self.game.display.blit(self.game.bg_img4, (0,0))
            self.game.draw_text("Credits", 40, self.half_w, self.half_h -100)
            self.game.draw_text("Created by:", 30, self.half_w, self.half_h + 10)
            self.game.draw_text("Magdalena Szymkowiak", 20, self.half_w, self.half_h +60)
            self.game.draw_text("Press <Backspace> to back to the main menu", 10, self.half_w, self.half_h + 270)
            self.game.draw_text("Production date: June 2021", 10, 100, 20)
            self.blit_screen()

class ScoresMenu(Menu):
    """
    Display view of the menu after pressing 'HighScores' on the main menu
    """
    def __init__(self,game):
        Menu.__init__(self,game)
    
    def show_menu(self):
        """
        Display High Scores from the game
        """
        self.display_run = True
        while self.display_run:
            self.game.handle_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.current_menu = self.game.main_menu
                self.display_run = False
            self.game.display.blit(self.game.bg_img4, (0,0))
            self.game.draw_text("High scores", 40, self.half_w, self.half_h -150)
            self.display_scores()
            self.game.draw_text("Press <Backspace> to back to the main menu", 10, self.half_w, self.half_h +270)
            self.blit_screen()

    def display_scores(self):
        """
        Display scores on the screen
        """
        pos_y= -50
        with open(Constant.list_scores,"r") as f:
            scores = json.load(f)
            scores= scores['HighScores']

        for i in range(1,6):
            self.game.draw_text(f"{i}."+ "  "+ self.check_len(i, str(scores[i-1])) , 30, self.half_w,self.half_h + pos_y)
            pos_y +=40

    def check_len(self,i,final):
        """
        Auxilary function in displaying adeqately numbers of dots
        """
        if len(final)==1:
            return "."*20 +" "+ final
        elif len(final)==2:
            return "."*19 +" "+ final
        elif len(final)==3:
            return "."*18 +" "+ final
        elif len(final)==4:
            return "."*17 +" "+ final

class GameOverMenu(Menu):
    """
    Menu after losing all of the lives
    """
    def __init__(self,game):
        """
        Initializing needed variables
        """
        Menu.__init__(self,game)
        self.state = "Restart"
        self.game_overx, self.game_overy = self.half_w, self.half_h -100
        self.scorex, self.scorey = self.half_w, self.half_h -25 
        self.restartx, self.restarty = self.half_w, self.half_h + 50
        self.main_menux, self.main_menuy = self.half_w, self.half_h + 100
        self.high_scorex, self.high_scorey = self.half_w, self.half_h + 150
        self.quitx, self.quity = self.half_w, self.half_h + 200
        self.msgx, self.msgy = self.half_w, self.half_h + 270
        self.cursor_rect.midtop = (self.restartx + self.offset, self.restarty)

    def open(self):
        """
        Open fresh gained score result
        """
        with open(Constant.this_score, "r") as f:
             return f.read()

    def show_menu(self):
        """
        Display the view of the widnow
        """
        score = self.open()
        self.display_run = True
        while self.display_run:
            self.game.handle_events()
            self.check_button()
            self.game.display.blit(self.game.bg_img4, (0,0))
            self.game.draw_text("Game over!!!", 40, self.game_overx, self.game_overy)
            self.game.draw_text("Score:" + score, 35,self.scorex, self.scorey, pygame.Color("red"))
            self.game.draw_text("Restart", 25, self.restartx, self.restarty)
            self.game.draw_text("Main Menu", 25, self.main_menux, self.main_menuy)
            self.game.draw_text("High Scores", 25,self.high_scorex, self.high_scorey)
            self.game.draw_text("Quit", 25,self.quitx, self.quity)
            self.game.draw_text("Press <up_arrow> to move cursor up and <down_arrow> to move it down", 10, self.msgx, self.msgy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        """
        Move cursor adequately to the event
        """
        if self.game.DOWN_KEY:
            self.game.menu_sound.play(0)
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
            self.game.menu_sound.play(0)
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
        """
        Check if buttons are pressed
        """
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