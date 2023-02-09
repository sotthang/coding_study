T = int(input())
for test_case in range(1, T + 1):
    memory = input()
    c = 0
    for x in range(len(memory)):
        if memory[x] == '1' and c == 0:
            c += 1
        elif memory[x-1] != memory[x] and c > 0:
            c += 1
    print(f'#{test_case} {c}')