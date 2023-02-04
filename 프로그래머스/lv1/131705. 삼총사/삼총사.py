def solution(number):
    answer = 0
    
    for x in range(len(number)-2):
        for y in range(x+1, len(number)-1):
            for z in range(y+1, len(number)):
                if (number[x]+number[y]+number[z]) == 0:
                    answer += 1
    return answer