T = int(input())
for test_case in range(1, T + 1):
    s = input()
    answer = []
    for x in s:
        if x not in answer:
            answer.append(x)
        else:
            answer.remove(x)
    if not answer:
        answer = 'Good'
    else:
        answer = ''.join(sorted(answer))
    print(f'#{test_case} {answer}')