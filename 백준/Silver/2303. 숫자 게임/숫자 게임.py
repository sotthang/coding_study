n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]
ans_list = []
for li in n_list:
    temp = 0
    for x in range(3):
        for y in range(x + 1, 4):
            for z in range(y + 1, 5):
                temp = max(temp, int(str(li[x] + li[y] + li[z])[-1]))
    ans_list.append(temp)
max_ans = ans_list[0]
ans = 0
for i in range(1, n):
    if ans_list[i] >= max_ans:
        max_ans = ans_list[i]
        ans = i

print(ans + 1)