PLACEHOLDER = '[name]'

# open up invited_names.txt and turn it into a list of names
with open('./Input/Names/invited_names.txt') as names_file:
    stripped_names = [name.strip() for name in names_file.readlines()]

# open letter up
with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    # replace '[name]' with list of names
    for name in stripped_names:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        # write letters to folder
        with open(f'./Output/ReadyToSend/letter_for_{name}.txt', 'w') as completed_letter:
            completed_letter.write(new_letter)



