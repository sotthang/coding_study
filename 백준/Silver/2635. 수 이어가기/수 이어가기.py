n = int(input())
ans = 0
ans_li = []
for x in range(1, n + 1):
    temp_li = [n, x]
    while temp_li[-1] >= 0:
        if temp_li[-2] - temp_li[-1] >= 0:
            temp_li.append(temp_li[-2] - temp_li[-1])
        else:
            break
    if ans < len(temp_li):
        ans = len(temp_li)
        ans_li = temp_li
print(ans)
print(*ans_li)