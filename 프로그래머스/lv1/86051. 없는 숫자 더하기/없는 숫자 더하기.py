def solution(numbers):
    all_number = set([1,2,3,4,5,6,7,8,9,0])
    return sum(all_number - set(numbers))