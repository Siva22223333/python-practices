#9. Reverse a dictionary (swap keys and values).

students = {
    "Manu": 85,
    "Ashwin": 92,
    "Kumar": 78,
    "David": 88
}

reversed_dict = {}

for key, value in students.items():
    reversed_dict[value] = key

print("Reversed Dictionary:")
print(reversed_dict)