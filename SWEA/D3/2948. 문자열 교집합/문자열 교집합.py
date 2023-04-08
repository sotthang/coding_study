T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    n_li = input().split()
    m_li = input().split()
    print(f'#{test_case} {n+m-len(set(n_li+m_li))}')