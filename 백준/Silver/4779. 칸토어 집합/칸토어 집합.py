def solve(n):
    if n == 1:
        return "-"
    else:
        left = solve(n // 3)
        center = " " * (n // 3)
        return left + center + left

while True:
    try:
        print(solve(3 ** int(input())))
    except EOFError:
        break