a, b = map(int, input().split())
li = [0]
for x in range(46):
    for _ in range(x):
        li.append(x)
print(sum(li[a : b + 1]))