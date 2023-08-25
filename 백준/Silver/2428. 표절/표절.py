n = int(input())
li = sorted(list(map(float, input().split())))
ans = 0
for x in range(n):
    l = x
    r = n
    while l < r:
        c = (l + r) // 2
        if li[x] >= li[c] * (0.9):
            l = c + 1
        else:
            r = c
    ans += r - x - 1
print(ans)