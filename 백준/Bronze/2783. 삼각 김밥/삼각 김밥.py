a, b = map(int, input().split())
ans = a / b * 1000
for _ in range(int(input())):
    c, d = map(int, input().split())
    if c / d * 1000 < ans:
        ans = c / d * 1000
print(round(ans, 2))