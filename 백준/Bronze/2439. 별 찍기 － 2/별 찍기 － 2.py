import sys

n = int(sys.stdin.readline())
for num in range(1, n+1):
    print(f'{"*"*num:>{n}}')