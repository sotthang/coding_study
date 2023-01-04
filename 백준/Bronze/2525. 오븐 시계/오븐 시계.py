hour, minute = map(int, input().split())
cook_time = int(input())
print((hour+cook_time//60+(minute+cook_time%60)//60)%24, (minute+cook_time%60)%60)