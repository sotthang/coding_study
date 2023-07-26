for _ in range(int(input())):
    s = input()
    coin = {
        "TTT": 0,
        "TTH": 0,
        "THT": 0,
        "THH": 0,
        "HTT": 0,
        "HTH": 0,
        "HHT": 0,
        "HHH": 0,
    }
    for x in range(38):
        coin[s[x : x + 3]] += 1
    print(*coin.values())