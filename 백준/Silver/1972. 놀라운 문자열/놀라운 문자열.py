while True:
    s = input()
    if s == "*":
        break

    for x in range(1, len(s) - 1):
        check = set()
        for y in range(len(s) - x):
            pairs = s[y] + s[y + x]
            if pairs in check:
                print(s, "is NOT surprising.")
                break
            else:
                check.add(pairs)
        else:
            continue
        break
    else:
        print(s, "is surprising.")