for t in range(1, int(input())+1):
    r, s = input().split()
    print(''.join([char * int(r) for char in s]))
