def is_prime_number(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    answer = n
    if is_prime_number(n):
        print(f'#{test_case} {answer-1}')
    else:
        for x in range(1, int(n**0.5) + 1):
            if n%x == 0 and x+n/x < answer:
                answer = x+n//x-2
        print(f'#{test_case} {answer}')