def solution(new_id):
    #1단계
    new_id = new_id.lower()
    #2단계
    for x in ("~!@#$%^&*()=+[{]}:?,<>/"):
        new_id = new_id.replace(x,"")
    #3단계
    while ".." in new_id:
        new_id = new_id.replace("..",".")
    #4단계
    new_id4 = new_id.strip(".")
    #5단계
    if len(new_id4) == 0:
        new_id4 = "a"
    #6단계
    if len(new_id4) >= 16:
        new_id4 = new_id4[:15]
        if new_id4[-1] == ".":
            new_id4 = new_id4[:-1]
    #7단계
    while len(new_id4) < 3:
        new_id4 += new_id4[-1]
    answer = new_id4
    return answer