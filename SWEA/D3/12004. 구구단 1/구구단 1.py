T = int(input())
nine_nine = []
for x in range(1, 10):
    for y in range(x, 10):
        nine_nine.append(x*y)
for test_case in range(1, T + 1):
    print(f'#{test_case} Yes') if int(input()) in nine_nine else print(f'#{test_case} No')