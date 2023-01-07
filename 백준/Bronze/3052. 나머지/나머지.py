import sys

count = set()

for _ in range(1, 11):
    count.add(int(sys.stdin.readline()) % 42)

print(len(count))