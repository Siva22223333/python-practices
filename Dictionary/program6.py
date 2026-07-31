#6. Check whether a key exists in a dictionary.

students = {
    "Manu": 85,
    "Ashwin": 92,
    "Kumar": 78,
    "David": 88
}

key = "Ashwin"

if key in students:
    print("Key exists.")
else:
    print("Key does not exist.")