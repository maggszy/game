from breakout import Breakout

if __name__ == "__main__":
    game = Breakout()
    #secure version
    #while True:  #this could change somehow
     #   game.handle_events()
      #  game.update()
       # game.draw()
    while game.running:
        game.current_menu.show_menu()
        #game.playing = True
        game.game_loop()
        #game.breakout_loop()
