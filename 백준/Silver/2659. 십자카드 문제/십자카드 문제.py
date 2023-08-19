def get_clock_num(n):
    min = int("".join(map(str, n)))
    for i in range(1, 4):
        tmp = int("".join(map(str, n[i:] + n[:i])))
        if min > tmp:
            min = tmp
    return min


answer = 1
for i in range(1111, get_clock_num(list(map(int, input().split())))):
    if "0" not in str(i) and i == get_clock_num(list(map(int, str(i)))):
        answer += 1
print(answer)