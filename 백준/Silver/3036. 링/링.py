def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

n = int(input())
circle = list(map(int, input().split()))
for x in range(1, n):
    g = gcd(circle[0], circle[x])
    print(f'{circle[0]//g}/{circle[x]//g}')