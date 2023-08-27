n, m = map(int, input().split())
n_ans, m_ans = 1, 1
for x in range(1, m + 1):
    n_ans *= n - x + 1
    m_ans *= x
print(n_ans // m_ans)