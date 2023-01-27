import sys

a, b = map(int, sys.stdin.readline().split())
a_set = set(list(map(int, sys.stdin.readline().split())))
b_set = set(list(map(int, sys.stdin.readline().split())))
print(len((a_set-b_set) | (b_set-a_set)))