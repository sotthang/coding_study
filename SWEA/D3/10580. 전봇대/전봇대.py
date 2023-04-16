T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    info = [[] for _ in range(N)]
    for i in range(N):
        info[i] = list(map(int, input().split()))
    result = 0
    for i1 in range(N-1):
        for i2 in range(i1+1, N):
            l1, r1 = info[i1]
            l2, r2 = info[i2]
            if (l1 > l2 and r1 < r2) or (l1 < l2 and r1 > r2):
                result += 1
    print(f'#{test_case} {result}')