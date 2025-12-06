import pandas

data = pandas.read_csv("NATO_Phonetic_Alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while KeyError:
    name = input("Enter a word: ").upper()
    try:
        output = [data_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(output)
        break

