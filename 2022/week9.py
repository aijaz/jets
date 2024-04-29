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
# https://bit.ly/JETSMay
# 5/12 Practice
# 5/14 Practice
# 5/15

# Project Task Breakdown
# ======================
# 1. Core Game Loop
# 2. Processing Input
# 3. Displaying the board
# 4. Display the keyboard Radi
# 5. Animations
# 6. Voiceover
# 7. Music???
# 8. Presentation - Kamron


# Functions
# kjlkjlkjkj()

# print("Hello, world")
# my_name = input("What is your name: ")
# print(f"Hello, {my_name}")
#
# print(my_name.upper())
# print(5)
# print([1, 2, 3])
# print("Hello", "Aijaz")

# def greet(name):
#     print(f"Hello, {name}")
#     print("Good to meet you.")
#     print("My name is Aijaz.")
#
# greet("Alice")
# greet("Bob")
# greet("Charlie")

# def double(single_thing):
#     return single_thing * 2
#
# print(double("Hey"))
# print(double(5))
#
# big_number = double(100)
# print(big_number)


# def add_em_up(num1, num2):
#     return num1 + num2
#
# the_sum = add_em_up(12, 33)
# print(the_sum)


# create a function called product that multiplies its two parameters (arguments) and returns the product

# def product(n1, n2):
#     return n1 * n2
#
# n = product(5, 3)
# print(n)


# def divide(numerator, denominator):
#     if denominator != 0:
#         return numerator // denominator
#     print("I can't do that")
#     return None
#
#
# n = int(input("Please enter the numerator: "))
# d = int(input("Please enter the denominator: "))
# result = divide(n, d)
# print(result)

# def process_secret_word(secret_word, guess):
#     result = []
#
#     for sw_letter, gw_letter in zip(secret_word, guess):
#         if sw_letter == gw_letter:
#             result.append('Y')
#         elif gw_letter in secret_word:
#             result.append('-')
#         else:
#             result.append('N')
#
#     return result
#
#
# secret_word = input("Please enter the secret word: ").upper()
#
# number_of_guesses = 0
# max_number_of_guesses = 6
#
# while number_of_guesses < max_number_of_guesses:
#     guess = input("Please enter the guess word: ").upper()
#     number_of_guesses = number_of_guesses + 1
#
#     if guess == secret_word:
#         print("That's right!!")
#         break
#
#     result = process_secret_word(secret_word, guess)
#     print(result)




class Shape:
    def __init__(self, num_sides=None):
        self.location = (0, 0)
        self.num_sides = num_sides

    def describe(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self):
        super().__init__(4)
        # self.num_sides = 4

    def describe(self):
        print(f"I am a rectangle and my location is {self.location}")


class Square(Rectangle):
    def __init__(self):
        super().__init__()

    def describe(self):
        print("I am a square")

class Triangle(Shape):
    def __init__(self):
        super().__init__(3)
        # self.num_sides = 3

    def describe(self):
        print(f"I am a triangle and I have {self.num_sides} sides")

class Circle(Shape):
    def __init__(self):
        super().__init__()

    def describe(self):
        print("I am a circle")


s1 = Shape()
print(s1.location)
s1.location = (1, 0)
print(s1.location)
s1.describe()

r1 = Rectangle()
print(r1.location)
r1.describe()

sq1 = Square()
print(sq1.num_sides)
sq1.describe()

t1 = Triangle()
print(t1.num_sides)
print(t1.location)
t1.describe()
t1.num_sides = 4
t1.describe()

c = Circle()
print(c.num_sides)
