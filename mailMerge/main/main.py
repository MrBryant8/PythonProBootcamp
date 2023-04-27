PLACEHOLDER = "[name]"

# File manipulation
with open("Input/Names/invited_names.txt") as f:
    names = f.readlines()

with open("Input/Letters/starting_letter.txt") as f1:
    content = f1.read()
    for name in names:
        stripped_name = name.strip()
        new_doc = content.replace(PLACEHOLDER, stripped_name)
        with open("./Output/ReadyToSend/letter_to_{}.txt".format(stripped_name), "w") as done_letter:
            done_letter.write(new_doc)
