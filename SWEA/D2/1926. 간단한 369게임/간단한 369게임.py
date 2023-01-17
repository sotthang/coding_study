for x in range(1, int(input())+1):
    count_369 = str(x).count('3')+str(x).count('6')+str(x).count('9')
    if count_369 > 0:
        x = count_369 * '-'
    print(x, end=' ')