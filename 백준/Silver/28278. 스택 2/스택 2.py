import sys

input = sys.stdin.readline
stack = []
for _ in range(int(input())):
    c = list(map(int, input().split()))
    if c[0] == 1:
        stack.append(c[1])
    elif c[0] == 2:
        print(stack.pop()) if stack else print(-1)
    elif c[0] == 3:
        print(len(stack))
    elif c[0] == 4:
        print(0) if stack else print(1)
    elif c[0] == 5:
        print(stack[-1]) if stack else print(-1)