triangle_list = [int(input()), int(input()), int(input())]
if triangle_list.count(60) == 3:
    print('Equilateral')
elif sum(triangle_list) == 180 and len(set(triangle_list)) == 2:
    print('Isosceles')
elif sum(triangle_list) == 180:
    print('Scalene')
else:
    print('Error')