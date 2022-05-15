# List Comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = 'roland'.title()
letters = [letter for letter in name]
print(letters)

doubled = [num * 2 for num in range(1, 5)]
print(doubled)

names = ['Amy', 'Beth', 'Rick', 'Caroline', 'Eleanor', 'Maddox']
long_and_upper = [name.upper() for name in names if len(name) > 4]
print(long_and_upper)
