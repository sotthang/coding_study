def gcd_two_numbers(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def solution(arr):
    LCMarr = arr[0]
    for x in range(len(arr)-1):
        GCDarr = gcd_two_numbers(LCMarr, arr[x+1])
        LCMarr = LCMarr * arr[x+1] // GCDarr
    return LCMarr