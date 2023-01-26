def solution(nums):
    answer = 0
    for x in range(len(nums)-2):
        for y in range(x+1, len(nums)-1):
            for z in range(y+1, len(nums)):
                for a in range(2, ((nums[x]+nums[y]+nums[z])//2)+1):
                    if (nums[x]+nums[y]+nums[z]) % a == 0:
                        break
                    elif a == (nums[x]+nums[y]+nums[z])//2:
                        answer += 1
    return answer