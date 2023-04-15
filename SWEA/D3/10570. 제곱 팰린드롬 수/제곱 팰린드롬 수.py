def palidrome(word):
    return str(word) == str(word)[::-1]

T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    a, b = map(int, input().split())
    for x in range(a, b+1):
        x_squareroot = x**0.5
        if x_squareroot != int(x_squareroot):
            continue
        elif palidrome(int(x_squareroot)) and palidrome(x):
            answer += 1
    print(f'#{test_case} {answer}')