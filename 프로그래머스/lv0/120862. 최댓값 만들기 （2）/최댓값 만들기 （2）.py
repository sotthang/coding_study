def solution(numbers):
    plus_numbers = sorted(numbers)[-1] * sorted(numbers)[-2]
    minus_numbers = sorted(numbers)[0] * sorted(numbers)[1]
    return plus_numbers if plus_numbers > minus_numbers else minus_numbers