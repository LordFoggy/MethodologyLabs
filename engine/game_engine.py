def run_game(play_game_fn):
    rounds = 3
    for _ in range(rounds):
        play_game_fn()
