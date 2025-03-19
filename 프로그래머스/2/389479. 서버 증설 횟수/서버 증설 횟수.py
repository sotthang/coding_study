def solution(players, m, k):
    answer, server = 0, [0] * len(players)
    
    for time in range(len(players)):
        unhandled_players = players[time] - (server[time] * m)
        
        if unhandled_players >= m:
            
            for serv_add_time in range(time, min(time + k, len(players))):
                server[serv_add_time] += unhandled_players // m
                
            answer += unhandled_players // m
            
    return answer