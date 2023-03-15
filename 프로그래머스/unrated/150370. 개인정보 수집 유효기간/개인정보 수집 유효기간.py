def solution(today, terms, privacies):
    answer = []
    for index, i in enumerate(privacies):
        a, b = i.split()
        for j in terms:
            if b in j:
                terms_m = int(j.split()[1])
                y, m, d = map(int, a.split('.'))
                m += terms_m
                if m > 12:
                    y += (m-1)//12
                    m = m%12
                    if m == 0:
                        m = 12
        privacies_ymd = f'{y}.{str(m).zfill(2)}.{str(d).zfill(2)}'
        if today >= privacies_ymd:
            answer.append(index+1)        
    return answer