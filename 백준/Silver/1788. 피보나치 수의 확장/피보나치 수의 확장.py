n = int(input())
pib = [0, 1]
for x in range(2, abs(n)+1):
    pib.append((pib[x-1] + pib[x-2]) % 1000000000)
if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(pib[abs(n)])