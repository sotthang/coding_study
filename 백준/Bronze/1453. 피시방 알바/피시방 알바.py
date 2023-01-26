people = int(input())
peolple_seat = list(map(int, input().split()))
print(len(peolple_seat) - len(set(peolple_seat)))