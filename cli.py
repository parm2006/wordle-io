import os
from wordle.game import WordleGame
from wordle.colors import Colors

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(f"\n{Colors.BOLD}TERMINAL WORDLE{Colors.RESET}")
    print("Guess the 5-letter word in 6 tries.")
    print("After each guess, the color of the tiles will change to show how close your guess was.")
    print("Green: Correct letter in correct spot")
    print("Yellow: Correct letter in wrong spot")
    print("Gray: Letter not in the word\n")

def print_hard_mode_info():
    print(f"{Colors.BOLD}HARD MODE:{Colors.RESET} Any revealed hints must be used in subsequent guesses.\n")

def play_game():
    clear_screen()
    print_header()

    while True:
        mode = input("Choose game mode (N)ormal or (H)ard: ").strip().upper()
        if mode in ['N', 'NORMAL']:
            hard_mode = False
            break
        elif mode in ['H', 'HARD']:
            hard_mode = True
            print_hard_mode_info()
            break
        else:
            print("Invalid choice. Please enter 'N' for Normal or 'H' for Hard mode.")

    game = WordleGame(hard_mode=hard_mode)

    while not game.game_over:
        clear_screen()
        print_header()
        if hard_mode:
            print_hard_mode_info()

        print(game)

        guess = input("Enter your guess: ").strip().lower()
        success, message = game.guess(guess)

        if not success:
            input(f"{message} Press Enter to continue...")

    clear_screen()
    print_header()
    if hard_mode:
        print_hard_mode_info()

    print(game)
    print(f"\n{Colors.BOLD}{message}{Colors.RESET}")

    play_again = input("\nPlay again? (Y/N): ").strip().upper()
    if play_again == 'Y':
        play_game()