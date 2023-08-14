hurt_finger = int(input())
count = int(input())

if 2 <= hurt_finger <= 4:
    if count % 2 == 0:
        print((count * 4) + (hurt_finger - 1))
    else:
        print((count * 4) + (5 - hurt_finger))
elif hurt_finger == 1:
    print(count * 8)
else:
    print(count * 8 + 4)