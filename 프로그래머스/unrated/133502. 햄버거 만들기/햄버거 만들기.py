def solution(ingredient):
    answer = 0
    hamburger = list()
    
    for x in ingredient:
        hamburger.append(x)
        if hamburger[-4:] == [1, 2, 3, 1]:
            answer += 1
            hamburger.pop()
            hamburger.pop()
            hamburger.pop()
            hamburger.pop()
    
    return answer