li=[4,3,6,7,2,5,7,2,9,7]
result = []
for x in li:
    if x not in result:
        result.append(x)

print(result)