def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_dict = {x: 0 for x in id_list}
    
    for r in set(report):
        a,b = r.split()
        report_dict[b] += 1
        
    for r in set(report):
        a,b = r.split()
        if report_dict[b] >= k:
            answer[id_list.index(a)] += 1

    return answer