def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)
c = 0
for x in str(factorial(int(input())))[::-1]:
    if x == '0':
        c += 1
    else:
        break
print(c)