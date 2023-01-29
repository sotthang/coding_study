def solution(numbers, hand):
    answer = ''
    position = {
        1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2], '*':[3, 0], 0: [3, 1], '#': [3, 2]
    }
    last_left = position['*']
    last_right = position['#']
    
    for x in numbers:
        if x in [1, 4, 7]:
            answer += 'L'
            last_left = position[x]
        elif x in [3, 6, 9]:
            answer += 'R'
            last_right = position[x]
        else:
            distance_left = abs(last_left[0]-position[x][0]) + abs(last_left[1]-position[x][1])
            distance_right = abs(last_right[0]-position[x][0]) + abs(last_right[1]-position[x][1])
            
            if distance_left < distance_right:
                answer += 'L'
                last_left = position[x]
            elif distance_left > distance_right:
                answer += 'R'
                last_right = position[x]
            else:
                if hand == 'left':
                    answer += 'L'
                    last_left = position[x]
                else:
                    answer += 'R'
                    last_right = position[x]
    
    return answer