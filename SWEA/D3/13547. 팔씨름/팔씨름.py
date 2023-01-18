T = int(input())
for test_case in range(1, T + 1):
    if input().count('x') < 8:
        answer = 'YES'
    else:
        answer = 'NO'
    print(f'#{test_case} {answer}')