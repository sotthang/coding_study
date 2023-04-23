import sys
from collections import defaultdict

dance = defaultdict(bool)
dance['ChongChong'] = True
answer = 1

for _ in range(int(sys.stdin.readline())):
    A, B = sys.stdin.readline().split()
    if dance[A]:
        if not dance[B]:
            dance[B] = True
            answer += 1
    elif dance[B]:
        dance[A] = True
        answer += 1

print(answer)