import pandas

data = pandas.read_csv("NATO_Phonetic_Alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Enter your name: ").upper()
output = [data_dict[letter] for letter in name]
print(output)