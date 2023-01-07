import sys

for _ in range(int(sys.stdin.readline())):
    student = list(map(int, sys.stdin.readline().split()))
    avg = sum(student[1:])/student[0]
    count = 0
    for x in student[1:]:
        if x > avg:
            count += 1
    print(f'{count / student[0] * 100:.3f}%')