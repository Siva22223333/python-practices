#5. Convert a tuple into a list, append an element, and convert it back.

numbers = (10, 20, 30, 40)

numbers_list = list(numbers)

numbers_list.append(50)

numbers = tuple(numbers_list)

print("Updated Tuple:", numbers)