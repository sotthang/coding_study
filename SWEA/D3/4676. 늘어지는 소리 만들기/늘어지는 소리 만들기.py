T = int(input())

for test_case in range(1, T + 1):
    s = input()
    h = int(input())
    li = sorted(list(map(int, input().split())))
    i = 0
    for x in li:
        x += i
        i += 1
        s = s[:x] + '-' + s[x:]
    print(f'#{test_case} {s}')