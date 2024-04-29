import random


def get_random_word():
    with open("secretwords.txt") as f:
        words = f.read().splitlines()

    return random.choice(words).upper()


def process_secret_word(secret_word, guess):
    result = []

    for sw_letter, gw_letter in zip(secret_word, guess):
        if sw_letter == gw_letter:
            result.append('🟩')
        elif gw_letter in secret_word:
            result.append('🟧')
        else:
            result.append('⬛️')

    return result


def print_history(h):
    for guess, result in h:
        print(guess, result)


"""
int a = 1;
while (a < 6) { 
   a += 1;
   printf("a is %d", a);
}
"""

while True:
    number_of_guesses = 0
    max_number_of_guesses = 6
    history = []

    secret_word = 'PITCH' # get_random_word()

    while number_of_guesses < max_number_of_guesses:
        guess = input(f"Please enter guess # {number_of_guesses + 1}").upper()
        number_of_guesses = number_of_guesses + 1

        result = process_secret_word(secret_word, guess)
        history.append((guess, "".join(result)))
        print_history(history)

        if guess == secret_word:
            print("That's right!!")
            break



    print("The word is ", secret_word)





