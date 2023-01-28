def solution(n, lost, reserve):
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)
    for x in _reserve:
        if x-1 in _lost:
            _lost.remove(x-1)
        elif x+1 in _lost:
            _lost.remove(x+1)
    return n - len(_lost)