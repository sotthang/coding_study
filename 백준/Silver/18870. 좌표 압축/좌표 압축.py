import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
x_sort = sorted(set(x))
x_dict = {x_sort[i]:i for i in range(len(x_sort))}
for xn in x:
    print(x_dict[xn], end=' ')