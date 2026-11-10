import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("./Day 26/nato_phonetic_alphabet.csv")
letter_dict = {row["letter"]:row["code"] for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
output_list = [letter_dict[word_letter] for word_letter in user_input]
print(output_list)