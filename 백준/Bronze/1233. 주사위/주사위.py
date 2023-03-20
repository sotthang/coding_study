s1, s2, s3 = map(int, input().split())
temp = {}
for x in range(1, s1+1):
    for y in range(1, s2+1):
        for z in range(1, s3+1):
            if x+y+z not in temp:
                temp[x+y+z] = 1
            else:
                temp[x+y+z] += 1
print(sorted(temp.items(), key=lambda x: x[1], reverse=True)[0][0])