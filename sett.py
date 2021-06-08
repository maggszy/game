class Constant:
    """
    Contain constant of the whole application
    """
    screen_height = 600
    screen_width = 800
    UP_KEY, DOWN_KEY, START_KEY, BACK_KEY = False, False, False, False
    start_lives = 5
    paddle_speed = 6
    collision_treshold = 12
    ball_maxspeed = 7
    brick_start = 36 
    brick_cols = 12
    brick_rows = 5
    this_score = "data/this_score.txt"
    list_scores = "data/leaderboard.json"