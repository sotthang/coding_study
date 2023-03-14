def solution(wallpaper):
    temp_x = []
    temp_y = []
    for x, a in enumerate(wallpaper):
        for y, b in enumerate(a):
            if b == '#':
                temp_x.append(x)
                temp_y.append(y)
    answer = [min(temp_x), min(temp_y), max(temp_x)+1, max(temp_y)+1]
    return answer