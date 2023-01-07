import sys

for _ in range(int(sys.stdin.readline())):
    point = 0
    for x in str(sys.stdin.readline())[:-1].split('X'):
        point += len(x)*(len(x)+1)//2
    print(point)