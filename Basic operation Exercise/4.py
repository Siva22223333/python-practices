# Swapping values

A = int(input("enter the First Number :- "))
B = int(input("enter the Second Number :- "))

print(f" The Values Before swapping  a = {A} and b= {B}")

A, B = B, A
print(f" The Values After swapping a ={A} and b = {B} ")
