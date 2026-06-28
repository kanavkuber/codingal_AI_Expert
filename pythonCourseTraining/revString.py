# 1) Ask the user to enter a word or sentence and store it in string.
string = input("Enter a word or sentence: ")

# 2) Create an empty string called string2.
string2 = ""

# 3) Loop through each character i in string.
for i in string:
    # Add the character i in front of string2.
    string2 = i + string2

# 4) Print the original string.
print("Original string:", string)

# 5) Print the reversed string.
print("Reversed string:", string2)