# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Readline function returns all lines of file as a list, in which each line is an item of the list.
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Replace function is used to replace a specific phrase of the string with another phrase.
# Hint3: His method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# Strip function is used to remove all the leading and trailing characters of the string.
# By default, it removes all the spaces.
with open("Input/Names/invited_names.txt") as f:
    name_list = f.readlines()
    print(name_list)

strip_name_list = []
for line in name_list:
    strip_name_list.append(line.strip("\n"))

print(strip_name_list)

with open("Input/Letters/starting_letter.txt", "r") as file:
    content = file.read()

print(content)

for name in strip_name_list:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as f:
        new_content = content.replace("[name]", name)
        f.write(new_content)

