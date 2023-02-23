T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    t = n-m
    print(f'#{test_case} {m+m-n} {t}')