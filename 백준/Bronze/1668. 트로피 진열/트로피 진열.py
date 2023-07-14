n = int(input())
li = [int(input()) for _ in range(n)]
l, r = 1, 1
for x in range(n - 1):
    if max(li[: x + 1]) < li[x + 1]:
        l += 1
    if max(li[n - x - 1 :]) < li[n - x - 2]:
        r += 1
print(l)
print(r)