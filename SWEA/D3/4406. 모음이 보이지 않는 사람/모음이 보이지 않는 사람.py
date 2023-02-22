T = int(input())
for test_case in range(1, T+1):
    n = input()
    n = n.translate(n.maketrans('aeiou', '11111')).replace('1','')
    print(f'#{test_case} {n}')