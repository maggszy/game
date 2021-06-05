from breakout import Breakout

if __name__ == "__main__":
    game = Breakout()
    while True:  #this could change somehow
        game.handle_events()
        game.update()
        game.draw()
