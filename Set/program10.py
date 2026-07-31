#10. Remove all duplicate characters from a string using a set.

text = "programming"

unique_characters = set(text)

result = ""

for char in unique_characters:
    result += char

print("Unique Characters:", result)
