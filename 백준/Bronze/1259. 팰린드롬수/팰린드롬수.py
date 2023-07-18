while True:
    n = input()
    if n == "0":
        break
    for x in range((len(n) // 2) + 1):
        if n[x] != n[len(n) - x - 1]:
            print("no")
            break
    else:
        print("yes")