def star(n):
    if n == 1:
        return ['*']
    stars = star(n//3)
    star_list = []
    for s in stars:
        star_list.append(s*3)
    for s in stars:
        star_list.append(s+' '*(n//3)+s)
    for s in stars:
        star_list.append(s*3)
    return star_list

print('\n'.join(star(int(input()))))