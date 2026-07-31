#6,Find the second largest number in a list.

numbers = [12, 45, 7, 89, 23, 56, 90, 34]
largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest:", second)

