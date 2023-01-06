import sys

n, x = map(int, sys.stdin.readline().split())

for z in list(filter(lambda y:y<x, list(map(int, sys.stdin.readline().split())))):
    print(z, end=' ')