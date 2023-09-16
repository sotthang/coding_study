x, y = map(int, input().split())
z = (y * 100) // x
if z > 98:
    print(-1)
    exit()
s = 0
e = x
while s < e:
    m = (s + e) // 2
    if (y + m) * 100 // (x + m) != z:
        e = m
    else:
        s = m + 1
print((s + e) // 2)