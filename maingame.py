from breakout import Breakout

if __name__ == "__main__":
    game = Breakout()
    while game.running:
        game.current_menu.show_menu()
        game.game_loop()

