import sys

prime_list = []

for num in range(1, 123456*2+1):
    for x in range(2, int(num**0.5)+1):
        if num % x == 0:
            break
    else:
        prime_list.append(num)

while True:
    n = int(sys.stdin.readline())
    c = 0
    if n == 0:
        break
    for x in prime_list:
        if n < x <= 2*n:
            c += 1
        elif x >= 2*n+1:
            break
    print(c)