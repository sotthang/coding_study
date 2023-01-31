room_list = [input() for _ in range(int(input()))]
w_answer, l_answer = 0, 0
for row in room_list:
    for x in row.split('X'):
        if x.count('.') >= 2:
            w_answer += 1
trans_room_list = list(zip(*room_list))
for col in trans_room_list:
    for y in ''.join(col).split('X'):
        if y.count('.') >= 2:
            l_answer += 1
print(w_answer, l_answer)