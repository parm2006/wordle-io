import random
import sys
from collections import Counter

# --- Constants ---
WORD_LENGTH = 5
MAX_GUESSES = 6
# NEW: Define separate file paths
ANSWER_LIST_FILE = "wordle_answers.txt"      # Words the answer can be chosen from
ALLOWED_LIST_FILE = "wordle_allowed_guesses.txt" # All valid words allowed for guessing

# ANSI escape codes for colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RESET = "\033[0m" # Resets the color

# --- Functions ---

def load_words(filepath):
    """Loads words from a file, filters for valid length, converts to lowercase."""
    try:
        with open(filepath, 'r') as f:
            # Read all lines, strip whitespace, convert to lowercase
            words = [word.strip().lower() for word in f.readlines()]
            # Filter for words of the correct length consisting only of letters
            valid_words = {
                word for word in words
                if len(word) == WORD_LENGTH and word.isalpha()
            }
            # Check if any valid words were found in this specific file
            if not valid_words:
                print(f"Warning: No {WORD_LENGTH}-letter words found in '{filepath}'.")
                # Don't exit here, maybe the other file is sufficient,
                # but let the main logic check if answers are missing.
            return valid_words
    except FileNotFoundError:
        print(f"Error: Word list file '{filepath}' not found.")
        print("Please ensure this file exists in the same directory.")
        sys.exit(1) # Exit if file not found
    except Exception as e:
        print(f"An error occurred loading words from '{filepath}': {e}")
        sys.exit(1)

def get_feedback(guess, secret_word):
    """Calculates the color feedback for a guess against the secret word."""
    # (This function remains the same as before)
    if len(guess) != WORD_LENGTH:
        return None

    feedback = ["_"] * WORD_LENGTH
    colored_guess = [""] * WORD_LENGTH

    secret_counts = Counter(secret_word)
    guess_copy = list(guess)

    for i in range(WORD_LENGTH):
        if guess_copy[i] == secret_word[i]:
            feedback[i] = "G"
            colored_guess[i] = f"{GREEN}{guess_copy[i].upper()}{RESET}"
            secret_counts[guess_copy[i]] -= 1
            guess_copy[i] = None

    for i in range(WORD_LENGTH):
        if guess_copy[i] is not None:
            if guess_copy[i] in secret_counts and secret_counts[guess_copy[i]] > 0:
                feedback[i] = "Y"
                colored_guess[i] = f"{YELLOW}{guess_copy[i].upper()}{RESET}"
                secret_counts[guess_copy[i]] -= 1
            else:
                feedback[i] = "X"
                colored_guess[i] = f"{GRAY}{guess_copy[i].upper()}{RESET}"

    return "".join(colored_guess)

# MODIFIED: Function now accepts the separate word sets
def play_game(answer_words, allowed_words):
    """Main game loop, using separate answer and allowed word lists."""
    secret_word = random.choice(list(answer_words))
    # print(f"(DEBUG: Secret word is {secret_word})") # Uncomment for debugging

    guesses_made = []
    feedback_history = []

    print("\n--- Welcome to Wordle Clone (Text-Based) ---")
    print(f"Guess the {WORD_LENGTH}-letter word. You have {MAX_GUESSES} tries.")

    for i in range(MAX_GUESSES):
        guess_num = i + 1
        print("-" * 20)
        print(f"Guess {guess_num}/{MAX_GUESSES}")

        # Display previous guesses
        for g_idx in range(len(guesses_made)):
             print(f"  {guesses_made[g_idx]} -> {feedback_history[g_idx]}")

        # Get and validate input
        while True:
            guess = input("Enter your guess: ").lower().strip()
            if len(guess) != WORD_LENGTH:
                print(f"Guess must be {WORD_LENGTH} letters long. Try again.")
            elif not guess.isalpha():
                print("Guess must only contain letters. Try again.")
            # MODIFIED: Check against the allowed_words set
            elif guess not in allowed_words:
                print("Not in allowed word list. Try again.")
            else:
                break # Valid guess received

        # Calculate and store feedback
        colored_result = get_feedback(guess, secret_word)
        guesses_made.append(guess.upper())
        feedback_history.append(colored_result)

        # Check for win
        if guess == secret_word:
            print("-" * 20)
            print(f"\nCongratulations! You guessed the word: {GREEN}{secret_word.upper()}{RESET}")
            print(f"It took you {guess_num} guess(es).")
            for g_idx in range(len(guesses_made)):
                print(f"  {guesses_made[g_idx]} -> {feedback_history[g_idx]}")
            return

    # If loop finishes, player lost
    print("-" * 20)
    print("\nGame Over! You didn't guess the word.")
    print(f"The secret word was: {YELLOW}{secret_word.upper()}{RESET}")
    for g_idx in range(len(guesses_made)):
            print(f"  {guesses_made[g_idx]} -> {feedback_history[g_idx]}")

# --- Main Execution ---
if __name__ == "__main__":
    # Load both word lists
    print(f"Loading answers from '{ANSWER_LIST_FILE}'...")
    answer_words_set = load_words(ANSWER_LIST_FILE)
    print(f"Loading allowed guesses from '{ALLOWED_LIST_FILE}'...")
    allowed_guesses_set = load_words(ALLOWED_LIST_FILE)

    # Crucial Check: Ensure the answer list has usable words
    if not answer_words_set:
        print(f"Error: No valid {WORD_LENGTH}-letter words found in the answer list '{ANSWER_LIST_FILE}'. Cannot play.")
        sys.exit(1)

    # Important: Ensure all possible answers are also considered allowed guesses
    # The `update` method adds all elements from answer_words_set into allowed_guesses_set
    # without duplicates (because they are sets).
    original_allowed_count = len(allowed_guesses_set)
    allowed_guesses_set.update(answer_words_set)
    if len(allowed_guesses_set) > original_allowed_count:
         print(f"Note: Added {len(allowed_guesses_set) - original_allowed_count} words from the answer list to the allowed guesses list.")


    print(f"Loaded {len(answer_words_set)} possible answers.")
    print(f"Loaded {len(allowed_guesses_set)} allowed guesses (including answers).")


    # Pass both sets to the game function
    play_game(answer_words_set, allowed_guesses_set)
    print("\nThanks for playing!")