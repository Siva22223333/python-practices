# Fizzbuzz
n = int(input("Enter the limit: "))

for i in range(1, n + 1):
    if i % 2 == 0 and i % 4 == 0:
        print("Fizz")
    elif i % 3 == 0 and i % 6 == 0:
        print("Buzz")
    elif i % 5 == 0:
        print("FizzBuzz")
    elif i == 7:
        print("seven")
    else:
        print(i)
