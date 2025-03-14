"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 20 minutes
Actual:   15 minutes

"""

text = input("Text: ")
words = text.split()
word_to_count = {}

# count ocurrences
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

# find the length of the longest word
longest_word_length = max(len(word) for word in word_to_count)

# sort and print
for word in sorted(word_to_count):
    print(f"{word:{longest_word_length}} : {word_to_count[word]}")
