import sys

guitar = []
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().rstrip()
    n_sum = 0
    for i in s:
        if i.isdigit():
            n_sum += int(i)
    guitar.append((s, n_sum))
guitar.sort(key=lambda x:(len(x[0]),x[1],x[0]))

for x in guitar:
    print(x[0])