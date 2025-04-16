from wordle.word_list import get_random_word, is_valid_word
from wordle.colors import colorize_guess, Colors

class WordleGame:
    def __init__(self, hard_mode=False):
        self.target_word = get_random_word()
        self.guesses = []
        self.max_attempts = 6
        self.hard_mode = hard_mode
        self.game_over = False
        self.won = False

    def guess(self, word):
        word = word.lower()
        if self.game_over:
            return False, "Game is already over."
        if not is_valid_word(word):
            return False, "Not in word list."
        if len(word) != len(self.target_word):
            return False, f"Word must be {len(self.target_word)} letters."
        if self.hard_mode and self.guesses:
            hard_mode_error = self._check_hard_mode_constraints(word)
            if hard_mode_error:
                return False, hard_mode_error
        self.guesses.append(word)
        if word == self.target_word:
            self.game_over = True
            self.won = True
            return True, f"Correct! You got it in {len(self.guesses)}/{self.max_attempts}."
        if len(self.guesses) >= self.max_attempts:
            self.game_over = True
            return True, f"Game over. The word was {self.target_word}."
        return True, ""

    def _check_hard_mode_constraints(self, new_guess):
        last_guess = self.guesses[-1]
        for i in range(len(self.target_word)):
            if last_guess[i] == self.target_word[i] and new_guess[i] != self.target_word[i]:
                return f"Letter {last_guess[i].upper()} must be in position {i+1}."
        for i in range(len(last_guess)):
            if last_guess[i] in self.target_word and last_guess[i] != self.target_word[i]:
                if last_guess[i] not in new_guess:
                    return f"Guess must contain the letter {last_guess[i].upper()}."
        return None

    def display_guesses(self):
        return "\n".join(colorize_guess(guess, self.target_word) for guess in self.guesses)

    def display_keyboard(self):
        keyboard = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        letter_status = {}
        for guess in self.guesses:
            for i, letter in enumerate(guess):
                letter = letter.upper()
                if letter not in letter_status:
                    letter_status[letter] = Colors.GRAY
                if guess[i] == self.target_word[i]:
                    letter_status[letter] = Colors.GREEN
                elif letter.lower() in self.target_word and letter_status[letter] != Colors.GREEN:
                    letter_status[letter] = Colors.YELLOW
        result = ""
        for row in keyboard:
            result += " "
            for letter in row:
                color = letter_status.get(letter, Colors.RESET)
                result += f"{color}{letter}{Colors.RESET} "
            result += "\n"
        return result

    def get_remaining_attempts(self):
        return self.max_attempts - len(self.guesses)

    def __str__(self):
        return f"\n{self.display_guesses()}\n\n{self.display_keyboard()}\nAttempts remaining: {self.get_remaining_attempts()}/{self.max_attempts}\n"