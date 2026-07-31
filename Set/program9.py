#9. Count the number of unique words in a sentence using a set.

sentence = "Noorul islam college for higher education"

words = sentence.split()

unique_words = set(words)

print("Unique Words:", unique_words)
print("Count:", len(unique_words))
