import sys
a, b = map(int, sys.stdin.readline().split())
n, m = 0, 0
while a > 0:
    n += a%10
    a //= 10
while b > 0:
    m += b%10
    b //= 10
print(n*m)