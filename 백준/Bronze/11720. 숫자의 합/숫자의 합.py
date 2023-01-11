import sys

n = int(sys.stdin.readline())
num = int(sys.stdin.readline())
answer = 0
while num > 0:
    answer += num%10
    num //= 10
print(answer)