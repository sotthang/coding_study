T = int(input())
for test_case in range(1, T + 1):
    num = input()
    count = 2
    answer = 'impossible'
    while len(num) == len(str(int(num)*count)):
        if sorted(num) == sorted(str(int(num)*count)):
            answer = 'possible'
            break
        count += 1
    print(f'#{test_case} {answer}')