def solution(rsp):
    rsp_dict = {"0":"5", "2":"0", "5":"2"}
    return ''.join([rsp_dict.get(x) for x in rsp])