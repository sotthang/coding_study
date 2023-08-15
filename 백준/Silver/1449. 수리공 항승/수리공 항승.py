n, l = map(int,input().split())
taped, count = 0,0
for x in sorted(list(map(int,input().split()))):
    if x > taped:
        count += 1
        taped = x+l-1
print(count)