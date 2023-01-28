def solution(answers):
    test1 = [1, 2, 3, 4, 5]
    test2 = [2, 1, 2, 3, 2, 4, 2, 5]
    test3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer1, answer2, answer3 = 0, 0, 0
    answer = []
    for x in range(len(answers)):
        if answers[x] == test1[x%5]:
            answer1 += 1
        if answers[x] == test2[x%8]:
            answer2 += 1
        if answers[x] == test3[x%10]:
            answer3 += 1
    max_answer = max(answer1, answer2, answer3)
    if max_answer == answer1:
        answer.append(1)
    if max_answer == answer2:
        answer.append(2)
    if max_answer == answer3:
        answer.append(3)
    return answer