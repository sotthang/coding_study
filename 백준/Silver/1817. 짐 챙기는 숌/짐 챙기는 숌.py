n, m = map(int, input().split())
t, ans = 0, 0
if n != 0:
    for x in list(map(int, input().split())):
        if t + x <= m:
            t += x
        else:
            ans += 1
            t = x
print(ans) if t == 0 else print(ans + 1)