def solution(land):
    for x in range(1, len(land)):
        for y in range(len(land[0])):
            land[x][y] += max(land[x-1][:y] + land[x-1][y+1:])
    return max(land[len(land)-1])