wood = list(map(int, input().split()))
sort_wood = sorted(wood)

while wood != sort_wood:
    for x in range(4):
        if wood[x] > wood[x+1]:
            wood[x], wood[x+1] = wood[x+1], wood[x]
            print(*wood)