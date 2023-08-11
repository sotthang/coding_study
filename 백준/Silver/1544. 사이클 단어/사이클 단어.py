li = []
for _ in range(int(input())):
    n = input()
    for x in range(len(n)):
        if n[x:] + n[:x] in li:
            break
    else:
        li.append(n)
print(len(li))