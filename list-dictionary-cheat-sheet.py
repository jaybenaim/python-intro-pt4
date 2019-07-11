a = '----------------------------------------------------'
colours = ["green", "purple", "orange"]
colours = ["green", "purple", "orange"]

print(type(colours))

print(len(colours))

print(colours[2])

print(type(colours[2]))

print(colours[0].upper())

colours[2] = "yellow"

print(colours)
print(colours[-1])

print(colours[-2])
print(a)
# colours[3]

greeting = "hello"

greetings = [greeting, "hi", "what's up?"]

print(greetings[0])

print(greetings[1])

number = 2

print(greetings[number])

print(greetings[-1])


print(a)
grades = [87, 65, 90, 77, 90]

print(len(grades))

grades.sort()

print(grades)

grades.reverse()

print(grades)

grades.count(90)

grades.count(77)

# grades.count(100)

grades.index(77)

grades.index(90)

# grades.index(100)
print(a)
print(max(grades))

print(min(grades))

# mixed = [1, 2, "A+"]

# print(min(mixed))

# mixed.sort()
print(a)
numbers = [1,5,22,100]

for current_num in numbers:
  # all these steps will happen once for each number:
  double = current_num * 2
  double_plus_one = double + 1
  no_more_than_one_hundred = max(100, double_plus_one)
  message = "Your score is {}%".format(no_more_than_one_hundred)
  print(message)

# un-indent to end the loop
print("This message displays just once after the loop is done")






print(a)
grades_list = [50, 77, 90, 95, 65]
total = 0

for grade in grades_list:
  total = total + grade

average = total / len(grades_list)
print("The class average is {}.".format(average))

grades_list = [50, 77, 90, 95, 65]

for index, grade in enumerate(grades_list):
  grades_list[index] = grade + 1

print(grades_list) # 51, 78, 91, 96, 66
print(a)
foods = ['rice', 'potatoes', 'noodles']

for current_index, current_food in enumerate(foods):
  print("{} is at position {}".format(current_food, current_index))
print(a)
for character_index, character in enumerate("hello"):
  print(f"index of {character} is {character_index}" )

# h
# e
# l
# l
# o
    
print(a)

my_dictionary = {
  'python': 'a big snake',
  'cat': 'a fluffy friend',
  'sheep': 'looks like a cloud'
}

my_dictionary['octopus'] = 'intelligent sea creature with 8 legs'
my_dictionary['octopus'] # 'intelligent sea creature with 8 legs'
my_dictionary.get('dog', None) # returns None instead of erroring
my_dictionary.get('cat', None) # returns 'a fluffy friend'
my_dictionary.pop('sheep') # 'looks like a cloud; a bit smelly''octopus': 'intelligent sea creature with 8 legs'}


print(my_dictionary) # {'python': 'a big snake', 'cat': 'a fluffy friend', 'octopus': 'intelligent sea creature with 8 legs'}
print(a)
print(my_dictionary.keys()) # dict_keys(['python', 'cat',  'octopus'])
my_dictionary.values() # dict_values(['a big snake', 'a fluffy friend', 'intelligent sintelligent sea creature with 8 legs'])

print(a)

for key, val in my_dictionary.items():
  print("{} ----> {}".format(key, val))

# python ----> a big snake
# cat ----> a fluffy friend
# octopus ----> intelligent sea creature with 8 legs

print(a) 
list_with_dict = [
  {'apple': 'fruit', 'carrot': 'vegetable'},
  {'winter': 'cold', 'summer': 'hot'}
]
mixed_list = [
  [1,2,3],
  {'one': 1, 'two': 2}
]
dict_with_list = {
  'numbers': [8,5,3],
  'words': ['hi', 'bye']
}

dict_with_dict = {
  'foods': {'apple': 'fruit', 'carrot': 'vegetable'},
  'seasons': {'winter': 'cold', 'summer': 'warm'}
}