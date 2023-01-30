import sys

def merge_sort(li):
    if len(li) == 1:
        return li
    
    center = (len(li)+1)//2
    left = merge_sort(li[:center])
    right = merge_sort(li[center:])
    i,j = 0,0
    li_2 = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            li_2.append(left[i])
            answer.append(left[i])
            i += 1
        else:
            li_2.append(right[j])
            answer.append(right[j])
            j+=1
    while i < len(left):
        li_2.append(left[i])
        answer.append(left[i])
        i += 1
    while j < len(right):
        li_2.append(right[j])
        answer.append(right[j])
        j += 1
    
    return li_2

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
answer = []
merge_sort(a)

print(answer[k-1]) if len(answer) >= k else print(-1)