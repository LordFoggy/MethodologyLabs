from games.game1 import play_game as play_game_1
from games.game2 import play_game as play_game_2
from engine.game_engine import run_game

if __name__ == "__main__":
    print("Welcome to the games!")
    while True:
        print("Choose a game:")
        print("1. Game 1 (Find the smallest common multiple)")
        print("2. Game 2 (Find the missing number in the progression)")
        print("0. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            run_game(play_game_1)
        elif choice == "2":
            run_game(play_game_2)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
