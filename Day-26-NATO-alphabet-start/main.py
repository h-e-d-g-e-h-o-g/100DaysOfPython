# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas

# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
print(nato_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def take_input():
    user_input = input("Enter a string:").upper()
    try:
        code_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only the letters in the alphabet please.")
        take_input()
# code_list = []
    else:
        print(code_list)
take_input()
# for letter in letters:
#     for (key, value) in nato_dict.items():
#         if letter == key:
#             code_list.append(value)
#
# code_list = [code for letter in letters for (key, code) in nato_dict.items() if letter == key]
# print(code_list)
