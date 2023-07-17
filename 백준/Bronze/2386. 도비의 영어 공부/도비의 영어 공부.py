while True:
    s = input()
    if s == "#":
        break
    print(s[0], s[2:].lower().count(s[0]))