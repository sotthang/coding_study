while True:
    a, b, c = sorted(map(int, input().split()))
    if a == 0:
        break
    elif a+b <= c:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == b or b == c or a == c:
        print('Isosceles')
    else:
        print('Scalene')