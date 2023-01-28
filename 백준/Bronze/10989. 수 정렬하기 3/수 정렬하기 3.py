import sys

c_list = [0] * 10001

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    c_list[num] += 1
    
for n in range(10001):
    if c_list[n] != 0:
        for _ in range(c_list[n]):
            print(n)