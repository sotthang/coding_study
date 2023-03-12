import sys

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]
temp = []
for x in range(n-1):
    temp.append(li[x+1] - li[x])
min_gcd = temp[0]
for y in range(1, n-1):
    min_gcd = gcd(min_gcd, temp[y])
print(((li[-1]-li[0])//min_gcd)-n+1)