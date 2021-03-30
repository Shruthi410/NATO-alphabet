
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_data = data.to_dict()

dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("What's the word? ").upper()
phonetic_list = [dictionary[letter] for letter in word]
print(phonetic_list)