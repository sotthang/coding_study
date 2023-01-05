import sys
t = int(sys.stdin.readline())
for num in range(1, t+1):
    x, y = map(int, sys.stdin.readline().split())
    print(f'Case #{num}: {x} + {y} =', x+y)