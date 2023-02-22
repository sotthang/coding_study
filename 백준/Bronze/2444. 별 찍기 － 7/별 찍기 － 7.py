n = int(input())
for x in range(n):
    print(' '*(n-x-1)+'*'*(2*x+1))
for y in range(n-1, 0, -1):
    print(' '*(n-y)+'*'*(2*y-1))