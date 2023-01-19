T = int(input())
for test_case in range(1, T + 1):
    s = input()
    for x in ['()', '(|', '|)']:
        s = s.replace(x, 'o')
        c = s.count('o')
    print(f'#{test_case} {c}')