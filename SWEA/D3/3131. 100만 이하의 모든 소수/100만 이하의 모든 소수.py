for x in range(2, 1000001):
    for y in range(2, int(x**0.5)+1):
        if x%y == 0:
            break
    else:
        print(x, end=' ')