for _ in range(int(input())):
    a, b = map(int, input().split())
    answer = a*b
    while b > 0:
        a, b = b, a%b
    print(answer//a)