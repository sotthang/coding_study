import sys

s = sys.stdin.readline().rstrip()
for _ in range(int(sys.stdin.readline())):
    a, l, r = sys.stdin.readline().split()
    print(s[int(l):int(r)+1].count(a))
