n = int(input())
li = list(map(int, input().split()))
s = int(input())
ans = 0
for x in li:
    if x != 0:
        if x % s == 0:
            ans += x // s
        else:
            ans += (x // s) + 1

print(ans * s)