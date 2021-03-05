import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')
#TODO create dictionary from DataFrame in format {'A':'Alfa'}
df_dict = {row.letter: row.code for (index, row) in df.iterrows()}

#TODO create list of phonetic code words from user input
word = input("Enter a word: ").upper()
nato_response = [df_dict[letter] for letter in word]
print(nato_response)
