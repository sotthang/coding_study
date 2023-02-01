for num in range(int(input()), 3, -1):
    for n in str(num):
        if n != '7' and n != '4':
            break
    else:
        print(num)
        break