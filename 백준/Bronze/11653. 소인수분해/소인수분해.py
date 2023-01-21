n = int(input())
num = 2
while (num**2 <= n):
    while (n % num == 0):
        print(num)
        n = n // num
    num += 1
if n > 1 :
    print(n)