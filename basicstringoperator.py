# Take string input
text = input("Enter a string: ")

# Print the length of the string
print("Length of the string:", len(text))

# Print the first character (if the string is not empty)
if text:
    print("First character:", text[0])
else:
    print("The string is empty.")