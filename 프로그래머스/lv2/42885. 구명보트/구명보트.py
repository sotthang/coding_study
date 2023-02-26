def solution(people, limit) :
    answer = 0
    people.sort()
    start = 0
    last = len(people) - 1
    while start < last :
        if (people[last] + people[start]) <= limit:
            start += 1
            answer += 1
        last -= 1
    return len(people) - answer