n = sorted(list(map(int, input().split())))
for x in input():
    if x == "A":
        print(n[0], end=" ")
    elif x == "B":
        print(n[1], end=" ")
    elif x == "C":
        print(n[2], end=" ")