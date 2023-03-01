n = int(input())
rgb_li = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, len(rgb_li)):
    rgb_li[i][0] = min(rgb_li[i - 1][1], rgb_li[i - 1][2]) + rgb_li[i][0]
    rgb_li[i][1] = min(rgb_li[i - 1][0], rgb_li[i - 1][2]) + rgb_li[i][1]
    rgb_li[i][2] = min(rgb_li[i - 1][0], rgb_li[i - 1][1]) + rgb_li[i][2]
print(min(rgb_li[n-1][0], rgb_li[n-1][1], rgb_li[n-1][2]))