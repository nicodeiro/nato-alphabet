#TODO 1. Create a dictionary in this format:
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phoenetic_dict = {row.letter: row.code for(index, row) in data.iterrows()}
print(phoenetic_dict)

#TODO 2. Create a list of the phonetic code wordsl from a word that the user inputs.
word = input("Enter a word: ").upper()
result = [phoenetic_dict[letter_word] for letter_word in word]
print(result)