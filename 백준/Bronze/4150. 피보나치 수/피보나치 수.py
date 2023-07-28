fib = [0, 1, 1]
for _ in range(4800):
    fib.append(fib[-1] + fib[-2])
print(fib[int(input())])