n, w, h = map(int, input().split())
for _ in range(n):
    s = int(input())
    print("DA") if s <= (w**2 + h**2) ** 0.5 else print("NE")