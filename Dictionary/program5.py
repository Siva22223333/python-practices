#5. Merge two dictionaries.

dict1 = {
    "A": 10,
    "B": 20
}

dict2 = {
    "C": 30,
    "D": 40
}

merged = dict1.copy()
merged.update(dict2)

print("Merged Dictionary:")
print(merged)