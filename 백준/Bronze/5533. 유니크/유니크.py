ans = []
li = []
n = int(input())
for _ in range(n):
    ans.append(0)
    li.append(list(map(int, input().split())))
li = list(map(list, zip(*li)))
for x in li:
    for i, y in enumerate(x):
        if x.count(y) == 1:
            ans[i] += y
print(*ans, sep="\n")