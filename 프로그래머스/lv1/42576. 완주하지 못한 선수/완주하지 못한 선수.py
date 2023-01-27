def solution(participant, completion):
    count = 0
    participant.sort()
    completion.sort()
    for x in range(len(completion)):
        if participant[x] != completion[x]:
            return participant[count]
        else:
            count += 1
    return participant[-1]
        