n = int(input())
road_list = list(map(int, input().split()))
answer = []
c = 0
for i in range(len(road_list)-1):
    if road_list[i] < road_list[i+1] and (i == len(road_list)-2):
        c += road_list[i+1] - road_list[i]
        answer.append(c)
    elif road_list[i] < road_list[i+1]:
        c += road_list[i+1] - road_list[i]
    else:
        answer.append(c)
        c = 0
print(max(answer))