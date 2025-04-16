VALID_WORDS = [
    "apple", "beach", "chair", "dance", "eagle", "flame", "ghost", "heart", 
    "juice", "kite", "lemon", "music", "night", "ocean", "piano", "queen", 
    "river", "snake", "tiger", "union", "virus", "water", "young", "zebra",
    "adult", "brave", "crime", "dream", "earth", "focus", "grape", "happy",
    "image", "jelly", "karma", "logic", "magic", "novel", "order", "peace",
    "query", "react", "smile", "table", "uncle", "value", "waste", "yacht",
    "zesty", "aloud", "bloom", "craft", "delay", "exist", "fairy", "gloom",
    "honor", "input", "jolly", "kneel", "laser", "medal", "nurse", "olive",
    "prize", "quote", "right", "swift", "train", "urban", "voice", "witch"
]

TARGET_WORDS = VALID_WORDS.copy()

def is_valid_word(word):
    return word.lower() in VALID_WORDS

def get_random_word():
    import random
    return random.choice(TARGET_WORDS).lower()