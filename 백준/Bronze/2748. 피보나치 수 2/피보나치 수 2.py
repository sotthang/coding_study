fib = [0, 1]
for _ in range(90):
    fib.append(fib[-1] + fib[-2])
print(fib[int(input())])