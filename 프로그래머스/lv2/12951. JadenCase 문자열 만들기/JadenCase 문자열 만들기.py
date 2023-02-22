def solution(s):
    answer = ''
    for x in range(len(s)):
        if s[x].isdigit():
            answer += s[x]
        elif x == 0:
            answer += s[x].upper()
        elif s[x-1] == ' ':
            answer += s[x].upper()
        else:
            answer += s[x].lower()
    return answer