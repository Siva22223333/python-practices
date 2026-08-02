# Questions:
# 1, Print hello name
First_name = input("enter your first name :  ")
Second_name = input("enter the second name:  ")

# 2,concact the first and second name
Join = (First_name + " " + Second_name)
print(f"Hello {Join}, hope you are doing well")

# 3,Length of the character
result = (len(Join))
print(f"the total length of the name is {result}")

# 4,Upper case of the word
upper = (Join.upper())
print(f"The upper case for the {Join} is {upper}")

# 5,read the first ccharacter of the word and print it
read = (Join[0])
print(f"{read}")
