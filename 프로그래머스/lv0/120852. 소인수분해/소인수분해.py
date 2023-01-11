def solution(n):
    answer = []
    count = 2
    while (count**2 <= n):
        while(n%count == 0):
            answer.append(count)
            n = n//count
        count += 1
    if n > 1:
        answer.append(n)
    return sorted(list(set(answer)))