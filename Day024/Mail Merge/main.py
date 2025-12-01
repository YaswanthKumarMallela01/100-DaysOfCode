"""[Name] is in starting_letter.txt. We can use this as placeholder to replace it with
actual name"""
PLACEHOLDER = "[Name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    """Reads individual lines in the txt file. Keep those individual lines in list"""

    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()  # Strip off the excess spaces or new lines in the name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)  # Replaces the [Name] with actual name

        """Creates a new file for each of the names mentioned in invited_names.txt"""
        with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)