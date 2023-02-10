def palindrome(n):
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            return 0
    else:
        return 1

T = 10
for test_case in range(1, T + 1):
    length = int(input())
    answer = 0
    puzzle = [list(input()) for _ in range(8)]
    transpose_puzzle = list(zip(*puzzle))
    for x in range(8):
        for y in range(8-length+1):
            answer += palindrome(puzzle[x][y:y+length]) + palindrome(transpose_puzzle[x][y:y+length])
    print(f'#{test_case} {answer}')