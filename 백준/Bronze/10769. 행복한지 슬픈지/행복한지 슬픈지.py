s = input()
emo_happy = s.count(':-)')
emo_sad = s.count(':-(')
if emo_happy > emo_sad:
    print('happy')
elif emo_happy < emo_sad:
    print('sad')
elif emo_happy == emo_sad and emo_happy >= 1:
    print('unsure')
else:
    print('none')