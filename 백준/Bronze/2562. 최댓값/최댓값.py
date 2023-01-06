import sys

numbers_list = [int(sys.stdin.readline()) for _ in range(9)]
print(max(numbers_list))
print(numbers_list.index(max(numbers_list))+1)