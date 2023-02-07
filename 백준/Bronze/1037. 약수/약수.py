n = int(input())
if n == 1:
    print(int(input())**2)
else:
    li = sorted(list(map(int, input().split())))
    print(li[0]*li[-1])