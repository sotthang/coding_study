t = 1
while True:
    n = int(input())
    if n == 0:
        break
    n1 = n * 3
    if n1 % 2 == 0:
        n2 = n1 // 2
        s = "even"
    else:
        n2 = (n1 + 1) // 2
        s = "odd"
    n3 = n2 * 3
    n4 = n3 // 9
    print(f"{t}. {s} {n4}")
    t += 1