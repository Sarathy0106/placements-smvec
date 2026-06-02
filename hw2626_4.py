#4.Find duplicate characters.

string = input("Enter a string: ")
duplicates = set()
for char in string:
    if string.count(char) > 1:
        duplicates.add(char)    
if duplicates:
    print("Duplicate characters:", ", ".join(duplicates))
else:
    print("No duplicate characters found.")
        