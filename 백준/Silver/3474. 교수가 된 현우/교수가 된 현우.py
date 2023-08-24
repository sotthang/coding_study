import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    answer = 0
    i = 5
    while i <= n:
        answer += n // i
        i *= 5
    print(answer)