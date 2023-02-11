def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(factorial(m)//(factorial(n)*factorial(m-n)))