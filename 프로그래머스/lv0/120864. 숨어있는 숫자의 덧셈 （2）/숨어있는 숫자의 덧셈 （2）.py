import re

def solution(my_string):
    return sum([int(x) for x in re.split('[^0-9]', my_string) if x])