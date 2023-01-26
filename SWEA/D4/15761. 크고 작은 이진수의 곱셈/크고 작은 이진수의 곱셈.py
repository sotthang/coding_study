T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    M = '1'*a + '0'*b
    m = '1'*1 + '0'*b + '1'*(a-1)
    c = (bin(int(M, 2) * int(m, 2))).count('1')
    print(f'#{test_case} {c}')