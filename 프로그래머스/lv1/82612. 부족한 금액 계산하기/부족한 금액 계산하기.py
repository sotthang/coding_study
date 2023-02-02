def solution(price, money, count):
    answer = sum(x for x in range(count+1)) * price - money
    return answer if answer > 0  else 0