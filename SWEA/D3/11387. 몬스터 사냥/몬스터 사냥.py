T = int(input())
for test_case in range(1, T + 1):
    d, l, n = map(int, input().split())
    print(f'#{test_case} {d*n+d*l*n*(n-1)//200}')