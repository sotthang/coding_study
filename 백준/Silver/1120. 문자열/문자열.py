a, b = input().split()
if len(a) == len(b):
    answer = 0
    for x, y in zip(a, b):
        if x != y:
            answer += 1
    print(answer)
else:
    temp = []
    for i in range(len(b)-len(a)+1):
        temp_num = 0
        for x, y in zip(a, b[i:i+len(a)]):
            if x != y:
                temp_num += 1
        temp.append(temp_num)
    print(min(temp))