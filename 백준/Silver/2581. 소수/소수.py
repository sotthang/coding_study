m = int(input())
n = int(input())
sum, min = 0, n
for num in range(m, n+1):
    c = 0
    for x in range(2, int(num**0.5)+1):
        if num % x == 0:
            c += 1
            break
    if c == 0 and num != 1:
        sum += num
        if num < min:
            min = num
print(sum, min) if sum != 0 else print(-1)