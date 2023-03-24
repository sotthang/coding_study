T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    answer = 0
    speed = 0
    command = [list(map(int, input().split())) for _ in range(n)]
    for x in command:
        if x[0] == 0:
            answer += speed
        elif x[0] == 1:
            speed += x[1]
            answer += speed
        elif x[0] == 2:
            if speed != 0:
                speed -= x[1]
                answer += speed
    print(f'#{test_case} {answer}')