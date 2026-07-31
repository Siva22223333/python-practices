#8. Sort a dictionary by its values.

students = {
    "Manu": 85,
    "Ashwin": 92,
    "Kumar": 78,
    "David": 88
}

sorted_dict = dict(sorted(students.items(), key=lambda item: item[1]))

print("Dictionary Sorted by Values:")
print(sorted_dict)