import sys

prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

for _ in range(int(sys.stdin.readline())):
    count = 0
    n = int(sys.stdin.readline())
    for i in prime:
        if i >= n:
            break
        if not check[n - i] and i <= n-i:  # 순서만 다른거 counting 하지 않기 위해
            count += 1
    print(count)