m, n = map(int, input().split())
alpha = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "siv",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
}
numbers = {}
for x in range(m, n + 1):
    numbers[x] = " ".join([alpha[y] for y in str(x)])
ans = sorted(numbers.keys(), key=lambda x: numbers[x])
for y in range(0, n - m + 1, 10):
    print(*ans[y : y + 10])