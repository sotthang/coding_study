T = int(input())
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    guest = sorted(list(map(int, input().split())))
    answer = 'Possible'
    for i in range(n):
        if guest[i] // m * k < i + 1:
            answer = 'Impossible'
            break
    print(f'#{test_case} {answer}')