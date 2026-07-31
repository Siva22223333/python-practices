#6. Remove a specific element from a set safely.

numbers = {10, 20, 30, 40}

element = 20

if element in numbers:
    numbers.remove(element)

print("Updated Set:", numbers)