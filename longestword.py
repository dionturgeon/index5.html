# Take sentence input
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the longest word
if words:
    longest_word = max(words, key=len)
    print("Longest word:", longest_word)
else:
    print("No words found.")