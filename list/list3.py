li=[4,3,6,7,2,5,7,2,9,7]
even=0
odd =0
for i in range(0,len(li)):
    if li[i] % 2 == 0:
        even=even + 1
    else:
        odd =odd + 1
print(f"count of even is {even}")
print(f"count of odd is {odd}")