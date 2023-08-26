import sys

n = int(input())
n_li = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())
l, r, ans = 0, n - 1, 0

while l < r:
    tmp = n_li[l] + n_li[r]
    if tmp == x:
        ans += 1
    elif tmp < x:
        l += 1
        continue
    r -= 1
print(ans)
