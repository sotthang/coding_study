n = int(input())
a = list(map(int, input().split()))
answer = [0] * n
temp = 0
for i in sorted(set(a)):
    for j in list(filter(lambda x: a[x] == i, range(len(a)))):
        answer[j] = temp
        temp += 1
print(*answer)