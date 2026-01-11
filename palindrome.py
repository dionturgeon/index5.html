word = input("Enter a word: ")

# Reverse the string
reversed_word = word[::-1]

# Check if it's a palindrome
if word == reversed_word:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")