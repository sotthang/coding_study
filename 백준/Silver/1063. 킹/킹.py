king, stone, n = map(str, input().split())
king_index = [8-int(king[1]), ord(king[0])-65]
stone_index = [8-int(stone[1]), ord(stone[0])-65]
a_h_dict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}
dx_dy_dict = {'T':(-1, 0), 'B':(1, 0), 'L':(0, -1), 'R':(0, 1), 'LT':(-1, -1), 'LB':(1, -1), 'RT':(-1, 1), 'RB':(1, 1)}
for _ in range(int(n)):
    d = input()
    if (king_index[0] + dx_dy_dict[d][0]) < 0 or (king_index[1] + dx_dy_dict[d][1]) < 0 or (king_index[0] + dx_dy_dict[d][0]) > 7 or (king_index[1] + dx_dy_dict[d][1]) > 7:
        continue
    elif (king_index[0] + dx_dy_dict[d][0]) == stone_index[0] and (king_index[1] + dx_dy_dict[d][1]) == stone_index[1]:
        if (stone_index[0] + dx_dy_dict[d][0]) < 0 or (stone_index[1] + dx_dy_dict[d][1]) < 0 or (stone_index[0] + dx_dy_dict[d][0]) > 7 or (stone_index[1] + dx_dy_dict[d][1]) > 7:
            continue
        else:
            king_index[0] += dx_dy_dict[d][0]
            king_index[1] += dx_dy_dict[d][1]
            stone_index[0] += dx_dy_dict[d][0]
            stone_index[1] += dx_dy_dict[d][1]
    else:
        king_index[0] += dx_dy_dict[d][0]
        king_index[1] += dx_dy_dict[d][1]
print(chr(king_index[1]+65)+str(8-king_index[0]))
print(chr(stone_index[1]+65)+str(8-stone_index[0]))