import sys

for _ in range(3):
    s = 0
    for _ in range(int(sys.stdin.readline())):
        s += int(sys.stdin.readline())
    if s == 0:
        print(0)
    elif s > 0:
        print('+')
    else:
        print('-')