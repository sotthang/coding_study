T = int(input())
for test_case in range(1, T + 1):
    D, H, M = map(int, input().split())
    m = (D-11)*1440+(H-11)*60+M-11
    print(f'#{test_case} {m}') if m >= 0 else print(f'#{test_case} -1')