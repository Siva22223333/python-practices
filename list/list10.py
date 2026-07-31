numbers = [1, 2, 2, 3, 4, 3, 2, 5, 1]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for key, value in frequency.items():
    print(key, ":", value)