for _ in range(int(input())):
    input()
    a, b, c, d = map(int, input().split())
    a, b, c = sorted((a, b, c))
    s = a + b + c - d
    a1 = min(s // 3, a)
    s -= a1
    b1 = min(s // 2, b)
    print(a1 * b1 * (s - b1))