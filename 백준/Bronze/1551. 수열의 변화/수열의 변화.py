n, k = map(int, input().split())
li = list(map(int, input().split(",")))
for _ in range(k):
    for x in range(len(li) - 1):
        li[x] = li[x + 1] - li[x]
    li.pop()
print(*li, sep=",")