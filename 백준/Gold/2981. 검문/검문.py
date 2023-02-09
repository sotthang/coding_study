def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

n = int(input())
answer = []
m_list = sorted([int(input()) for _ in range(n)])
m_max = m_list[1] - m_list[0]

for x in range(1, n-1):
    m_max = gcd(m_list[x+1]-m_list[x], m_max)

for y in range(1, int(m_max**0.5)+1):
    if m_max % y == 0:
        if (y**2) != m_max:
            answer.append(m_max//y)
        if y != 1:
            answer.append(y)
print(*sorted(answer))