T = int(input())
for test_case in range(1, T + 1):
    num_list = []
    n = int(input())
    answer = 0
    while len(num_list) != 10:
        answer = str(int(answer) + n)
        for char in answer:
            if char not in num_list:
                num_list.append(char)
    print(f'#{test_case} {answer}')