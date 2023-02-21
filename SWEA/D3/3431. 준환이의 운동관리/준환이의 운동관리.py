T = int(input())
for test_case in range(1, T + 1):
    l, u, x = map(int, input().split())
    if x < l:
        print(f'#{test_case} {l-x}')
    elif l <= x <= u:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} -1')