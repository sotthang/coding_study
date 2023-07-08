a, b = map(str, input().split())
a1, a2, b1, b2 = (
    int(a.replace("6", "5")),
    int(a.replace("5", "6")),
    int(b.replace("6", "5")),
    int(b.replace("5", "6")),
)
print(a1 + b1, a2 + b2)