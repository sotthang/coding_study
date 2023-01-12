def solution(polynomial):
    x_count = 0
    num_count = 0
    for y in polynomial.split(' + '):
        if y.isnumeric():
            num_count += int(y)
        else:
            if len(y) > 1:
                x_count += int(y[:-1])
            else:
                x_count += 1
    if x_count == 0 and num_count == 0:
        return '0'
    elif x_count == 0:
        return f"{num_count}"
    elif x_count == 1:
        x_count = ''
    if num_count == 0:
        return f"{x_count}x"
    else:
        return f"{x_count}x + {num_count}"