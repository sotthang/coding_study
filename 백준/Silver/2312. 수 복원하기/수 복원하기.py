def factorization(x):
    li = {}
    n = 2
    while n <= x:
        if x % n == 0:
            if n in li:
                li[n] += 1
            else:
                li[n] = 1
            x /= n
        else:
            n += 1
    return li


for _ in range(int(input())):
    n = int(input())
    for k, v in factorization(n).items():
        print(k, v)