import sys

tri = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for x in range(10, 100):
    tri.append(tri[x-2] + tri[x-3])
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(tri[n-1])