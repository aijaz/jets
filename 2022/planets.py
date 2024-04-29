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

# for planet_name, num_moons in moon_info:
#     print(f"{planet_name} has {num_moons} moons")

# total = 0
# for planet_name, num_moons in moon_info:
#     total = total + num_moons
#
# print(f"The total number of moons in the solar system is {total}")
#
#
# print([num_moons for planet_name, num_moons in moon_info])
#
# print(sum([num_moons for planet_name, num_moons in moon_info]))

# total = 0
# for planet_name, num_moons in moon_info[-3:]:
#     print(f"{planet_name} has {num_moons} moons")
#     total = total + num_moons
#
# print(f"The total number of moons is {total}")

# # t = ("a", "b")
# first, second = ("a", "b")
# print(first)
# print(second)


# print([1 / number for number in range(1, 5)])


import pyttsx3
what = input("What should I say? ")
engine = pyttsx3.init()
engine.say(what)
engine.runAndWait()










