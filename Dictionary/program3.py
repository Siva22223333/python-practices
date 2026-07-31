

students = {
    "Manu": 85,
    "Ashwin": 92,
    "Kumar": 78,
    "David": 88
}

highest_student = max(students, key=students.get)

print("Top Student:", highest_student)
print("Marks:", students[highest_student])