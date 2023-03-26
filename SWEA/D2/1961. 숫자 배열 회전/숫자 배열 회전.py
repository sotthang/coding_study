T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{test_case}')
    for x in range(n):
        for a in range(n):
            print(li[n-1-a][x], end='')
        print('', end=' ')
        for b in range(n):
            print(li[n-1-x][n-1-b], end='')
        print('', end=' ')
        for c in range(n):
            print(li[c][n-1-x], end='')
        print(' ')