T = int(input())
for test_case in range(1, T + 1):
    s = input()
    answer = 1
    for x in range(len(s)//2):
        if s[x] != s[-x-1]:
            answer = 0
            break
    print(f'#{test_case} {answer}')