answer = []
station_sum = 0
for _ in range(4):
    get_on, got_off = map(int, input().split())
    station_sum += got_off - get_on
    answer.append(station_sum)
print(max(answer))