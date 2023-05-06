while True:
    s = input()
    if s == '#':
        break
    print(s.translate(s.maketrans("aeiouAEIOU", "1111111111")).count('1'))