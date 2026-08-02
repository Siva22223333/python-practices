# Multiplication table of two by using for loop

num = int(input("Enter the number:  "))
for i in range(1, 11):
    print(num * i)

# identify the vovels from the given sentence.

sentence = input("enter the sentence:   ")
print("Vowels in the sentence are as follows:")
for ch in sentence:
    if ch.lower() in "aeiou":
        print(ch)

    # factorial

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)
