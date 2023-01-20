T = int(input())
for test_case in range(1, T + 1):
    words = input()
    answer = 0
    for word, alphabet in zip(words, 'abcdefghijklmnopqrstuvwxyz'):
        if word == alphabet:
            answer += 1
        else:
            break
    print(f'#{test_case} {answer}')