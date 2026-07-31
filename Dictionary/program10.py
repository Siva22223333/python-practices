#10. Find the word that appears most frequently in a sentence.

sentence = "python is easy and python is powerful and python is popular"

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

most_frequent = max(frequency, key=frequency.get)

print("Most Frequent Word:", most_frequent)
print("Frequency:", frequency[most_frequent])