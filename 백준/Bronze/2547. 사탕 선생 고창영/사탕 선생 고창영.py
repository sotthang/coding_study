for _ in range(int(input())):
    x = input()
    n = int(input())
    s = 0
    for _ in range(n):
        s += int(input())
    print('YES') if s%n==0 else print('NO')