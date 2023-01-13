def solution(chicken):
    answer = 0
    while chicken >= 10:
        coupon = chicken // 10
        remain_coupon = chicken % 10
        answer += coupon
        chicken = coupon + remain_coupon
    return answer