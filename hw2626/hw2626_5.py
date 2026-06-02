#5.Remove special characters.

string = input("Enter a string: ")
cleaned_string = ""
for char in string:
    if char.isalnum() or char.isspace():
        cleaned_string += char
print("String without special characters:", cleaned_string)
    