import sys

card_list = list(range(1, int(sys.stdin.readline())+1))
while card_list:
    print(card_list[0], end=' ')
    card_list.pop(0)
    if card_list:
        card_list = card_list[1:] + [card_list[0]]