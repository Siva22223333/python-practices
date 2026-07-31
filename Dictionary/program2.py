#2. Print all keys and all values separately.

students = {
    "Manu": 85,
    "Ashwin": 92,
    "Kumar": 78,
    "David": 88
}

print("Keys:")
for key in students.keys():
    print(key)

print("\nValues:")
for value in students.values():
    print(value)