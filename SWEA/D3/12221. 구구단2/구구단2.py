T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'#{test_case} -1') if a >= 10 or b >= 10 else print(f'#{test_case} {a*b}')