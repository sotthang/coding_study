T = int(input())
for test_case in range(1, T + 1):
    s = input()
    n = 1
    while True:
        if s[0:n] == s[n:n+n]:
            break
        n += 1
    print(f'#{test_case} {n}')