import collections
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
c = collections.Counter(n_list)
print(' '.join(f'{c[x]}' if x in c else '0' for x in m_list))