def solution(s):
    answer = []
    for x in sorted(s[2:-2].split("},{"), key=len):
        for y in x.split(','):
            if int(y) not in answer:
                answer.append(int(y))
    return answer