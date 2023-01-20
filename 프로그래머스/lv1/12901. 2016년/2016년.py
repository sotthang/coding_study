def solution(a, b):
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[((sum(months[0:a-1]) + b-1) % 7)]