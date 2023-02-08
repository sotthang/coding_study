def solution(s):
    answer = 0
    x_first = s[0]
    x_count = 0
    other_count = 0
    for x in range(len(s)):
        if (s[x] == x_first) or (x_first == 0):
            x_count += 1
            x_first = s[x]
        else:
            other_count += 1
        if x_count == other_count:
            answer += 1
            x_count = 0
            other_count = 0
            x_first = 0
    if (x_count != 0) or (other_count != 0):
        answer += 1
    return answer