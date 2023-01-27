for test_case in range(int(input())):
    num = int(input())
    a, b = num//2, num//2
    while True:
        c = 0
        for n in range(2, int(a**0.5)+1):
            if a % n == 0:
                break
        else:
            c += 1
        for n in range(2, int(b**0.5)+1):
            if b % n == 0:
                break
        else:
            c += 1
        if c == 2:
            break
        else:
            a -= 1
            b += 1
    print(a, b)
    
        
