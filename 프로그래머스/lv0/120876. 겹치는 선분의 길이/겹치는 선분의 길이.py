def solution(lines):
    lines_dict = {}
    for x in lines:
        for y in range(x[0], x[1]):
            if int(y) + 0.5 not in lines_dict:
                lines_dict[int(y) + 0.5] = 1
            else:
                lines_dict[int(y) + 0.5] += 1
    return len([int(1) for x in lines_dict.values() if x > 1])