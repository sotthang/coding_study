import sys

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    while True:
        if is_prime(n):
            print(n)
            break
        else:
            n += 1