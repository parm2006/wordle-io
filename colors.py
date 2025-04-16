class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    GRAY = '\033[90m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def colorize_guess(guess, target):
    result = ""
    used_letters = {}

    for i in range(len(guess)):
        if guess[i] == target[i]:
            used_letters[target[i]] = used_letters.get(target[i], 0) + 1

    for i in range(len(guess)):
        if guess[i] == target[i]:
            result += f"{Colors.GREEN}{guess[i]}{Colors.RESET}"
        elif guess[i] in target:
            letter_count = target.count(guess[i])
            used_count = used_letters.get(guess[i], 0)
            if used_count < letter_count:
                result += f"{Colors.YELLOW}{guess[i]}{Colors.RESET}"
                used_letters[guess[i]] = used_count + 1
            else:
                result += f"{Colors.GRAY}{guess[i]}{Colors.RESET}"
        else:
            result += f"{Colors.GRAY}{guess[i]}{Colors.RESET}"
    return result