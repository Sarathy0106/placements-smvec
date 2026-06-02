#3.Count vowels and consonants.

vowels = "AEIOUaeiou"
vc = 0
cc = 0 
string = input("Enter a string: ")
for char in string:
    if char in vowels:
        vc+= 1
    else:
        cc += 1
print("Number of vowels:", vc)
print("Number of consonants:", cc)