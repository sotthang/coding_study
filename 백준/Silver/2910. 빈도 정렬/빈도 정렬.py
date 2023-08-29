n, c = map(int, input().split())
count = {}
for i, n in enumerate(list(map(int, input().split()))):
    if n in count:
        count[n][0] += 1
    else:
        count[n] = [1, i, n]
answer = []
for x in sorted(count.values(), key=lambda x: (-x[0], x[1])):
    answer += [x[2]] * x[0]
print(*answer)