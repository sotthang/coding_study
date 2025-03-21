def solution(schedules, timelogs, startday):
    def add_minutes(time: int, minutes: int) -> int:
        hour, minute = divmod(time % 100 + minutes, 60)
        return (time // 100 + hour) * 100 + minute

    answer = len(schedules)
    
    for sched, timel in zip(schedules, timelogs):
        for i, time in enumerate(timel):
            startd = (startday + i - 1) % 7 + 1
            if startd in {6, 7}:
                continue
            if add_minutes(sched, 10) < time:
                answer -= 1
                break
                
    return answer
