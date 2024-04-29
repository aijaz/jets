# 3/31
# Homework
# Break
# Dictionaries

# 3/31
# Homework
# Break
# Dictionaries

# 4/7
# HW
# Functions

# 4/14
# HW
# Classes

# 4/21 Text-based Wordle
# 4/28 Graphical Wordle
# 5/5 Voiceover Music and Graphics
# 5/12

# 5/15


moon_info = [
    ("Mercury", 0),
    ("Venus", 0),
    ("Earth", 1),
    ("Mars", 2),
    ("Jupiter", 80),
    ("Saturn", 83),
    ("Uranus", 27),
    ("Neptune", 14),
]
for planet_name, num_moons in moon_info:
    if num_moons > 20:
        print(f"{planet_name} has {num_moons} moons")


# 3. Pretend your computer has a name.
# Ask the user for their name.
# If the name they enter is the same as the computer's name,
# print "Hey! That's my name, too!".
# If not, print "That's a nice name."
# The comparison should be case-insensitive.

# if a < 5:
# if 5 < a:
# if 5 > a

# computer_name = "Bob"
# your_name = input("What is your name? ")
#
# if your_name.upper() == computer_name.upper():
#     print("Hey! That's my name, too")
# else:
#     print("That's a nice name.")
#

# Ask the user to input a command
# If the command is "Donate"
#  Print "What do you want to donate"
# Otherwise
#  Print "When would you like to volunteer?"

# command = input("Please enter a command: ")
#
# if command.lower() == "donate":
#     print("What do you want to donate?")
# else:
#     print("When would you like to volunteer")
#

# Team
#  Name
#  List of players
#  Strengths
#  Coaches
#  Win rate
#  Overall competitiveness


# bulls = {
#     "name": "Bulls",
#     "list_of_players": ["Jordan", "Pippen", "Grant", "Rodman", "Cartwright"],
#     "strengths": "Triangle Offense",
#     "head_coach": "Jackson",
#     "record": "72-10",
#     "overall": "dominant"
# }
#
# pistons = {
#     "name": "Pistons",
#     "list_of_players": ["Thomas", "Laimbeer", "Dumars"],
#     "strengths": "Physicality",
#     "head_coach": "Daly",
#     "record": "",
#     "overall": "dominant"
# }
#
# print(bulls)
#
# bulls["record"] = "52-30"
#
# print(bulls)
# print(bulls["overall"])
# print(bulls["best_player"])
#
#

aang = {"name": "Aang",
        "gender": 'M',
        "nationality": "Southern Air Temple",
        "children": [{'name': 'Bumi', 'gender': 'M'},
                     {'name': 'Kya', 'gender': 'F'},
                     {'name': 'Tenzin', 'gender': 'M'}]
        }

katara = {}

katara['name'] = "Katara"
katara['gender'] = "F"
katara['children'] = aang['children']

print(katara['children'])
aang['children'][1]['name'] = "Kiya"
print(aang['children'])
print(katara['children'])

for k in aang.keys():
    print(k)

for v in aang.values():
    print(v)

for aaa, bbb in aang.items():
    print(f"For Aang, his {aaa} is {bbb}")

for my_tuple in aang.items():
    yyy, zzz = my_tuple
    print(f"For Aang, his {yyy} is {zzz}")

for the_thing in aang:
    print(f"The value of {the_thing} is {aang[the_thing]}")

print([i.upper() for i in aang])