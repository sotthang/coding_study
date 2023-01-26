for test_case in range(int(input())):
    change = int(input())
    for num in [25, 10, 5, 1]:
        print(change//num, end=' ')
        change -= num*(change//num)
    print()