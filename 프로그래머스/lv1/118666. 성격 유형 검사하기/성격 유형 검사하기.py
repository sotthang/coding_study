def solution(survey, choices):
    answer = ""
    check = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    
    for x, y in zip(survey,choices):
        if y > 4:
            check[x[1]] += y-4
        elif y < 4:
            check[x[0]] += 4-y
    
    check_list = list(check.items())
    
    for x in range(0, 8, 2):
        if check_list[x][1] < check_list[x+1][1]:
            answer += check_list[x+1][0]
        else:
            answer += check_list[x][0]
    
    return answer