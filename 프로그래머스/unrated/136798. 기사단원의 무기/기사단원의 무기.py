def solution(number, limit, power):
    answer = 0
    
    for divisors in range(1, number+1):
        count = 0
        for divisor in range(1, int(divisors**(0.5)+1)):
            if divisors % divisor == 0:
                count += 1
                if (divisor**2) != divisors:
                    count += 1
        if count <= limit:
            answer += count
        else:
            answer += power
    
    return answer