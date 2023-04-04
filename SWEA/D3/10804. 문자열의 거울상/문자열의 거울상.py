T = int(input())
mirror_dict = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}
for test_case in range(1, T + 1):
    answer = ''
    for word in input()[::-1]:
        answer += mirror_dict[word]
    print(f'#{test_case} {answer}')