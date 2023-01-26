import sys

stack_list = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    stack_list.append(num) if num != 0 else stack_list.pop()
print(sum(stack_list))