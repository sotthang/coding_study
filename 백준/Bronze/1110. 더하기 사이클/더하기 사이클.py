import sys

count = 0
num = int(sys.stdin.readline())
answer = num
while True:
    a, b = num//10, num%10
    num = b*10 + (a+b)%10
    count += 1
    if num == answer:
        break
print(count)