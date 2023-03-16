def check(n):
    temp = []
    for x in n:
        if temp and ((temp[-1] == '[' and x == ']') or (temp[-1] == '{' and x == '}') or (temp[-1] == '(' and x == ')')):
            temp.pop()
        else:
            temp.append(x)
    return len(temp)

def solution(s):
    answer = 0
    for y in range(len(s)):
        if check(s) == 0:
            answer += 1
        s = s[1:] + s[0]
    return answer