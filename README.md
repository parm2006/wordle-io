# Terminal Wordle

A Python implementation of the popular Wordle game that runs in the terminal, using standard color-coded feedback. It requires separate files for potential answers and allowed guesses.

## Features

*   Play Wordle in your terminal with standard color-coded feedback.
*   Uses separate lists for possible answers and all allowed guess words.
*   Simple command-line interface.
*   No external dependencies required.

## Requirements

*   Python 3.6 or higher
*   Two text files located in the **same directory** as the `wordle_game.py` script:
    *   `wordle_answers.txt`: Contains one valid 5-letter **answer** word per line. The secret word will be chosen from this list.
    *   `wordle_allowed_guesses.txt`: Contains one valid 5-letter **guess** word per line. This list should include all words from `wordle_answers.txt`, plus any other valid words allowed for guessing.

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/parm2006/wordle-io.git
    cd wordle-io
    ```
    (If you are not cloning and just have the script, simply navigate to the directory containing `wordle_game.py`)

2.  **Prepare the Word Lists:**
    Ensure you have correctly named `wordle_answers.txt` and `wordle_allowed_guesses.txt` files (as described in Requirements) populated with words and placed in the *same directory* as `wordle_game.py`. You can often find suitable lists online specifically for Wordle answers vs. allowed guesses.

## How to Play

1.  **Navigate to the game directory** in your terminal (the one containing `wordle_game.py` and the word list files).

2.  **Run the game:**
    ```bash
    python wordle_game.py
    ```

3.  **Follow the prompts** to guess the 5-letter word within 6 tries.

4.  **Feedback Colors:** (Requires a terminal that supports ANSI color codes)
    *   🟩 `\033[92m`Green`\033[0m`: Correct letter in the correct spot.
    *   🟨 `\033[93m`Yellow`\033[0m`: Correct letter in the wrong spot.
    *   ⬜ `\033[90m`Gray`\033[0m` (or terminal default): Letter not in the word at all.

## License

MIT