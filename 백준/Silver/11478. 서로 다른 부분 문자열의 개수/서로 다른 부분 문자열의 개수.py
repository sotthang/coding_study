s = input()
li = []
for x in range(len(s)):
    for y in range(len(s)-x):
        li.append(s[x:x+y+1])
print(len(set(li)))