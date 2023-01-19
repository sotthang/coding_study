def solution(babbling):
    answer = 0
    
    for x in babbling:
        for y in ["aya", "ye", "woo", "ma"]:
            x = x.replace(y, " ")
        if x.isspace():
            answer += 1
    
    return answer