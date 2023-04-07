T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    for i in range(n):
        if not m & 1:
            answer = 'OFF'
            break
        m >>= 1
    else:
        answer = 'ON'
    print(f'#{test_case} {answer}')