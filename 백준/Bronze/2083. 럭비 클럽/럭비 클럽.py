while True:
    n, a, w = input().split()
    if n == '#':
        break
    elif int(a) > 17 or int(w) >= 80:
        print(f'{n} Senior')
    else:
        print(f'{n} Junior')