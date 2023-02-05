while True:
    xyz = sorted(list(map(int, input().split())))
    x, y, z = xyz[0], xyz[1], xyz[2]
    if x == 0 and y == 0 and z == 0:
        break
    print('right') if z**2 == (x**2 + y**2) else print('wrong')