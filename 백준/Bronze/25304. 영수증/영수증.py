total = int(input())
total_cal = 0
for _ in range(int(input())):
    price, amount = map(int, input().split())
    total_cal += price * amount
print('Yes') if total == total_cal else print('No')