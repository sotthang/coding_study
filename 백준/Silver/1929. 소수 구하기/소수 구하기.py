m, n = map(int, input().split())
for num in range(m, n+1):
    c = 0
    for x in range(2, int(num**0.5)+1):
        if num % x == 0:
            c += 1
            break
    if c == 0 and num != 1:
        print(num)