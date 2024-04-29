import random

list_of_valid_words = []


def populate_valid_words():
    global list_of_valid_words
    if len(list_of_valid_words) > 0:
        return
    with open("all5.txt") as f:
        list_of_valid_words = f.readline().split(",")


def process_words(secret_word, guess):
    if len(secret_word) == 5 and len(guess) == 5:
        populate_valid_words()
        if guess not in list_of_valid_words:
            return None

        # Create a list named `result`:
        result = []
        for secret_word_character, guess_character in zip(secret_word, guess):
            if secret_word_character == guess_character:
                result.append('Y')
            elif guess_character in secret_word:
                result.append('-')
            else:
                result.append('N')

        return result
    else:
        return None


def get_secret_word():
    with open("allcommonwords.txt") as f:
        words = f.read().splitlines()

    common_five = [word for word in words if len(word) == 5]

    return random.choice(common_five).upper()
