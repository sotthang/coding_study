n, k = map(int, input().split())

for x in range(1, n+1):
    if n%x == 0:
        k -= 1
    if k == 0:
        print(x)
        break
else:
    print(0)