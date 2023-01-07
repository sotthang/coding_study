import sys

number = [x for x in range(1, 31)]

for _ in range(1, 29):
    number.remove(int(sys.stdin.readline()))

print(number[0])
print(number[1])