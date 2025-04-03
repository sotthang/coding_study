def solution(data, ext, val_ext, sort_by):
    type = ["code", "date", "maximum", "remain"]
    answer = sorted(list(filter(lambda x: x[type.index(ext)] <= val_ext, data)), key=lambda y: y[type.index(sort_by)])
    return answer