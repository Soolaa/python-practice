with open("./Input/Names/invited_names.txt", "r") as names:
    name_list = names.readlines()

#print(name_list)

for name in name_list:
    name = name.strip()
    with open("./Input/Letters/starting_letter.txt", "r") as file:
        letter = file.read()
        letter = letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/{name}.invitation", "w") as final:
            final.write(letter)


