import sys
fb = [1, 2]
n = int(sys.stdin.readline())
for x in range(n-2):
    fb.append((fb[x]+fb[x+1])%15746)
print(fb[n-1])