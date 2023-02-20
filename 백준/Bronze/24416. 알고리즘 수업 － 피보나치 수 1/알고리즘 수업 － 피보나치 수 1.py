import sys
fibonacci = [1, 1]
n = int(sys.stdin.readline())
for x in range(n-2):
    fibonacci.append(fibonacci[x] + fibonacci[x+1])
print(fibonacci[-1], n-2)