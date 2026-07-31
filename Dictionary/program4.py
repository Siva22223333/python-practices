#4. Count the frequency of each character in a string using a dictionary.

text = "Noorul islam college for higher education"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequency:")

for key, value in frequency.items():
    print(key, ":", value)