def solution(operations):
    answer = []
    for x in operations:
        command, value = x.split()[0], int(x.split()[1])
        if command == 'I':
            answer.append(value)
        elif command == 'D' and len(answer) != 0:
            if value < 0:
                answer.pop(answer.index(min(answer)))
            else:
                answer.pop(answer.index(max(answer)))

    if not answer:
        return [0, 0]
    else:
        return [max(answer), min(answer)]