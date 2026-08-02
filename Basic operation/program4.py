# if else Questions
# 1,check positive or negative

number = int(input("enter the number to check:  "))
if (number > 0):
    print(f"The number {number} is a positive number")
else:
    print(f"The number {number} is a Negative number")

# 2,check whether even or odd.

if (number % 2 == 0):
    print(f"The number {number} is an even number")
else:
    print(f"The number {number} is an odd number")
""
# 3,Read Marks and print pass or fail(35 marks)(attendance>=75)

marks = int(input("enter the marks:  "))
attendance = int(input("enter the attendance:  "))
if (marks >= 35 and attendance >= 75):
    print("you have successfully passed the examination.")
else:
    print("Sorry!, unfortunately you haven't cleared the exam, try again")

# 4,Read age and check vote eligibility.

age = int(input("enter the age:  "))
citizen = input("are you a citizen. (yes/no):")
if (age >= 18 and citizen == "yes"):
    print("Your are eligible to vote")
else:
    print("You are not eligibe for votting")

# 5,read two numbers and print the bigger number.

number1 = int(input("enter the first number:  "))
number2 = int(input("enter the second number:  "))
if (number1 > number2):
    print(f"{number1} is bigger")
else:
    print(f"{number2} is bigger")
