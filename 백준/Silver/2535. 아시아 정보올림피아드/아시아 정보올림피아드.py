n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
li.sort(key=lambda x: x[-1], reverse=True)
for x in range(2):
    print(li[x][0], li[x][1])
for y in range(2, n):
    if li[0][0] != li[1][0]:
        print(li[y][0], li[y][1])
        break
    elif li[0][0] != li[y][0]:
        print(li[y][0], li[y][1])
        break