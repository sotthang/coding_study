T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    answer = 0
    for _ in range(n):
        a, b = map(float, input().split())
        answer += a*b
    print(f'#{test_case} {answer}')