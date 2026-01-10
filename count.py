sentence = input("Enter a sentence: ")

# Count words
words = sentence.split()
word_count = len(words)

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1

print("Number of words:", word_count)
print("Number of vowels:", vowel_count)My 