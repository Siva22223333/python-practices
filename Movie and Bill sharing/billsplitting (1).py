print("-"*50)
print("      BILL SPLITTING AMONG FRIENDS")
print("-"*50)

n = int(input("Enter the number of friends: "))

names = []

print("-"*50)
print("Enter Friends' Names")
print("-"*50)

for i in range(n):
    name = input("Friend " + str(i+1) + ": ")
    names.append(name)

bill = float(input("\nEnter the Total Bill Amount: "))

share = bill / n

print("-"*50)
print("BILL SUMMARY")
print("-"*50)

print("Total Bill Amount :", bill)
print("Number of Friends :", n)
print("Amount Per Friend :", round(share, 2))

print("-"*50)
print("PAYMENT DETAILS")
print("-"*50)

for i in names:
    print(i, "should pay ₹", round(share, 2))

print("-"*50)
print("THANK YOU!")
print("-"*50)