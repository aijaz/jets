# 3/24
# Homework
# Break
# Dictionaries

# 3/31
# Loops/Functions
# Break
# Homework

# 4/7 Week 9
# HW
# Functions/Classes

# 4/14
# Classes
# Text Wordle

# 4/21 Graphical Wordle Project
# 4/28 Graphical Wordle Project
# 5/5 Voiceover Music and Graphics
# 5/12 Practice
# 5/14 Practice
# 5/15

# Project Task Breakdown
# ======================
# 1. Core Game Loop
# 2. Processing Input
# 3. Displaying the board
# 4. Display the keyboard
# 5. Animations
# 6. Voiceover
# 7. Music???
# 8. Presentation - Kamron


# t_minus = 11
# while t_minus > 1:
#     t_minus = t_minus - 1
#     if t_minus % 2 == 1:
#         continue
#     print(t_minus)
#
#
# print("Liftoff!!!!")



# current_number = 0                                # cn
# while current_number < 3:                         #  0   1    2
#     current_number += 1                           #  1   2    3
#     if current_number == 2:                       #  F   T    F
#         continue                                  #  -   Y    -
#     print(current_number)                         #  Y        Y
#




# # a % b is the remainder of a / b
# for n in range(1, 101):
#     if n % 15 == 0:  # if n is a multiple of 15
#         if n % 2 == 0: # if n is a multiple of 2
#             continue
#         print(f"{n} is a multiple of 15")
#         for x in range(1, n+1):
#             if x % 7 == 0:
#                 if x % 2 == 0:
#                     continue
#                 print(f"   {x} is a multiple of 7")


# for n in range(1, 100):
#     for o in range(1, 100):
#         for p in range(1, 100):
#             print(f"{n}, {o}, {p}")
#


# days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
# for n, day in enumerate(days):
#     print(f"{day} is day {n+1}")
#

# eng = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
# spa =  ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab']
#
# for e, s in zip(eng, spa):
#     print(f"The Spanish word for {e} is {s}")
#


# Ask the user to enter a secret word
# Ask the user to enter a guess word
# Create a list named results
# For every letter in secret word:
#  if the letter is the same as in the secret word,
#    append Y to results
#  else if letter is in the secret word
#    append - to result
#  else if letter is not in secret word
#    append N to result
# print result

secret_word = input("Please enter the secret word: ").upper()

number_of_guesses = 0
max_number_of_guesses = 6

while number_of_guesses < max_number_of_guesses:
    guess = input("Please enter the guess word: ").upper()
    number_of_guesses = number_of_guesses + 1

    if guess == secret_word:
        print("That's right!!")
        break

    result = []

    for sw_letter, gw_letter in zip(secret_word, guess):
        if sw_letter == gw_letter:
            result.append('Y')
        elif gw_letter in secret_word:
            result.append('-')
        else:
            result.append('N')

    print(result)