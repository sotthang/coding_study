def solution(park, routes):
    answer = []
    ewsn = {'E':(0, 1), 'W':(0, -1), 'S':(1, 0), 'N':(-1, 0)}
    for i in range(len(park)):
        park[i] = 'X' + park[i] + 'X'
    park.insert(0, 'X'*(len(park[0])))
    park.append('X'*(len(park[0])))
    for i, p in enumerate(park):
        if 'S' in p:
            answer.extend([i, p.index('S')])
    for x in routes:
        d, n = x.split()
        temp_x, temp_y = 0, 0
        for i in range(1, int(n)+1):
            try:
                if park[answer[0]+temp_x+ewsn[d][0]][answer[1]+temp_y+ewsn[d][1]] != 'X':
                    temp_x += ewsn[d][0]
                    temp_y += ewsn[d][1]
                else:
                    temp_x, temp_y = 0, 0
                    break
            except:
                pass
        answer[0] += temp_x
        answer[1] += temp_y
    return [answer[0]-1, answer[1]-1]