import itertools

T = int(input())

for test_case in range(1, T + 1):
    li = []
    for x in itertools.combinations(sorted(list(map(int, input().split())), reverse=True), 3):
        li.append(sum(x))
    print(f'#{test_case} {sorted(set(li), reverse=True)[4]}')