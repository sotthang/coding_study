T = int(input())
d = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    print(f'#{test_case} {d[m2-1]+d2-d[m1-1]-d1+1}')