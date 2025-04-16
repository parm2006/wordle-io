# Terminal Wordle

A Python implementation of Wordle that runs in the terminal with colored feedback.

## Features

- Play Wordle in your terminal with color-coded feedback
- Normal and Hard mode gameplay
- Visual keyboard display showing letter statuses
- Simple and intuitive interface

## How to Play

1. Clone this repository
2. Run `python main.py` to start the game
3. Guess the 5-letter word in 6 tries
4. After each guess, the color of the tiles will change:
   - 🟩 Green: Correct letter in correct spot
   - 🟨 Yellow: Correct letter in wrong spot
   - ⬜ Gray: Letter not in the word

## Game Modes

- **Normal Mode**: Standard Wordle rules
- **Hard Mode**: Any revealed hints must be used in subsequent guesses

## Requirements

- Python 3.6 or higher
- No external dependencies needed

## Installation

```bash
git clone git@github.com:parm2006/terminal-wordle.git
cd terminal-wordle
python main.py
```

## License

MIT

