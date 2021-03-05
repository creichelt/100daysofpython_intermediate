#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open('Input/Names/invited_names.txt') as file:
    names = file.readlines()

with open('Input/Letters/starting_letter.txt') as template:
    contents = template.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = contents.replace('[name]', stripped_name)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as new_file:
            new_file.write(new_letter)
        print(new_letter)
