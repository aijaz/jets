from jets import *
#
# characters = [['Aang',
#                'Northern Air Temple',
#                ['Kya', 'Bumi', 'Tenzin'],
#                ['Air', 'Water', 'Earth', 'Fire']],
#               ['Katara',
#                'Southern Water Tribe',
#                ['Kya', 'Bumi', 'Tenzin'],
#                ['Water', 'Blood']]
#                ]
#
d = {"chair": "a piece of furniture",
     "zebra": "a black and white animal"
     }
# print(d['chair']) # key
# print(d['zebra'])
# d['chair'] = 'furniture you sit on'
# print(d['chair'])
# print(d)
# print(d.keys())
# for x in d.keys():
#     print(x)
# for x in d.items():
#     print(x)
# for x in d.values():
#     print(x)
# for x in d:
#     print(x)
# d['people'] = ['Alice', 'Bob', 'Charlie']
# print(d)

# characters = {}
# characters['Aang'] = {}
# print(characters)
# characters['Aang']['children'] = ['Kya', 'Bumi', 'Tenzin']
# characters['Aang']['country'] = "Northern Air Temple"
# characters['Aang']['bending'] = ['Air', 'Fire', 'Water', 'Earth']
# print(characters)
#
# print(len(characters['Aang']['children']))
# print(len(characters['Aang']['bending']))
# print(characters['Aang']['bending'])
# print(characters['Aang']['children'][0])
#
#
# # Add a definition for 'bag'. 'Something you put stuff in'
# # print the dictionary
# d['bag'] = "Something you put stuff in"
# print(d)

def say_hi():
     print("Hi")
     print("Good to meet ya")
     print("")

# say_hi()
# say_hi()
# say_hi()


def greet_person(name):
     print("Hi", name)

greet_person("Cameron")
greet_person("Malaya")

name = "Cameron"
print("Hi", name)
name = "Malaya"
print("Hi", name)

def introduce(name):
     print("My name is", name)

introduce("Aijaz")


def describe_pet(animal="goat", color="black"):
    print(f"I have a {color} {animal}")


describe_pet("cat", "black")
describe_pet("dog", "brown")
describe_pet("red", "fish")
describe_pet(color="yellow", animal="bird")
describe_pet("iguana")
describe_pet()
describe_pet(color="yellow")

print(describe_pet())

def add(a, b):
     return(a + b)

print(add(2, 7))
print(add(4, 14))
add(5, 20)


# Write a function called make_shirt() that
# accepts a size and the text of a message
# that should be printed on the shirt.
# The function should print a sentence
# summarizing the size of the shirt and
# the message printed on it.

def make_shirt(size="large", message="ilp"):
     print(f"This is a {size} shirt that says {message}")

make_shirt("large", "I like turtles")

make_shirt("large")
make_shirt("medium")
make_shirt("small", "ihc")
# Modify the make_shirt() function so that
# shirts are large by default with a message
# that reads I love Python. Make a large
# shirt and a medium shirt with the
# default message, and a shirt of any size
# with a different message.


# Make a function called city_country() that
# takes in the name of a city and its
# country. The function should return a
# string formatted like this: "Lima, Peru"
# Call your function with at least three
# city-country pairs, and print the values
# that are returned.

def city_country(city, country):
     return f"{city}, {country}"


print(city_country("Denver", "USA"))
print(city_country(country="Canada", city="Montreal"))
s = city_country(city="Cancun", country="Mexico")
print(s)


