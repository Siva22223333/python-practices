li=[4,3,6,7,2,5,7,2,9,7]
max=li[0]
for i in range(0,len(li)):
    if max < li[i]:
        max = li[i]

print("largest value in the list is -- ",max)