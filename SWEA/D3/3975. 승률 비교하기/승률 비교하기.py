T = int(input())
answer = []
for _ in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    if a/b > c/d:
        answer.append('ALICE')
    elif a/b < c/d:
        answer.append('BOB')
    else:
        answer.append('DRAW')
for test_case in range(T):
    print(f'#{test_case+1} {answer[test_case]}')