def solution(my_string):
    return "".join(list(map(lambda x: x.lower() if x.isupper() else x.upper(), [x for x in my_string])))