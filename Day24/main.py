# # long way to open and close files
# file = open('my_file.txt')
# contents_of_file = file.read()
# print(contents_of_file)
# file.close()

# more efficient way of opening and closing files
with open('/Users/rick/Desktop/my_file.txt') as file:
    contents = file.read()
    print(contents)

# writing to a file but overwrites everything
with open('my_file.txt', mode='w') as f:
    f.write('I am 32 years old.')

# appending to file without overwriting it
with open('my_file.txt', mode='a') as f:
    f.write('\nMy name is Rick.')
