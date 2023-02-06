k = int(input())
hexagon = [list(map(int, input().split())) for _ in range(6)]
w, w_index, h, h_index = 0, 0, 0, 0
for i, wh in enumerate(hexagon):
    if wh[0] == 1 or wh[0] == 2:
        if w < wh[1]:
            w = wh[1]
            w_index = i
    else:
        if h < wh[1]:
            h = wh[1]
            h_index = i
minus_rect = (hexagon[(w_index-1)%6][1] - hexagon[(w_index+1)%6][1]) * (hexagon[(h_index-1)%6][1] - hexagon[(h_index+1)%6][1])
print((w*h - abs(minus_rect))*k)