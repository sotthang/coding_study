def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

n, k = map(int, input().split())
print(min(count_number(n, 5) - count_number(k, 5) - count_number(n - k, 5), count_number(n, 2) - count_number(k, 2) - count_number(n - k, 2)))