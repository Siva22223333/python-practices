#10. Remove duplicate values by creating a new tuple.

numbers = (1, 2, 3, 2, 4, 5, 1, 6)

unique = ()

for num in numbers:
    if num not in unique:
        unique += (num,)

print("Tuple without duplicates:", unique)