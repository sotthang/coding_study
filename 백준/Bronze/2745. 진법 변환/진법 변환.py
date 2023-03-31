n, b = input().split(' ')
n, b = ''.join(reversed(n)), int(b)
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = 0
for x in range(len(n)-1, -1, -1):
    answer += num.index(n[x]) * (b**x)
print(answer)