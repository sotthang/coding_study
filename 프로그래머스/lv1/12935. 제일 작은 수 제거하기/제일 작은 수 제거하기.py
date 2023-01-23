def solution(arr):
    del arr[arr.index(min(arr))]
    return [-1] if not arr else arr