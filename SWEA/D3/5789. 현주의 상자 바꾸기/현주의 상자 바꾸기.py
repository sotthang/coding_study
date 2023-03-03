T = int(input())
for test_case in range(1, T + 1):
    n, q = map(int, input().split())
    li = [0] * n
    for x in range(1, q+1):
        l, r = map(int, input().split())
        li[l-1:r] = [x]*(r-l+1)
    print(f'#{test_case}', *li)