for _ in range(int(input())):
    n = int(input())
    fashion = {}
    for _ in range(n):
        x, y = input().split()
        if y not in fashion:
            fashion[y] = 1
        else:
            fashion[y] += 1
    c = 1
    for x in fashion:
        c *= fashion[x]+1
    print(c-1)