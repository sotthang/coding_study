for _ in range(int(input())):
    input()
    a, b, c, d = map(int, input().split())
    li = sorted([a, b, c])
    while d != 0:
        d -= 1
        li[-1] -= 1
        li.sort()
    print(li[0] * li[1] * li[2])