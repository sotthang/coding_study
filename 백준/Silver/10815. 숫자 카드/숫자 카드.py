import sys

n = int(sys.stdin.readline())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
for i in m_list:
    first = 0
    end = n-1
    mid = n//2
    while i != n_list[mid]:
        if first == end:
            print(0, end=' ')
            break
        if i < n_list[mid]:
            end = mid-1
        else:
            first = mid
        mid = (first+end+1)//2
    else:
        print(1, end=' ')