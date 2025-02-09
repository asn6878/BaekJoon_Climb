from collections import deque

def solution(tickets):
    path = dict()
    
    for i in tickets:
        if i[0] in path:
            path[i[0]].append(i)
        else:
            path[i[0]] = list([i])
    
    for key, val in path.items():
        val.sort()
    
    answer = list()
    current = "ICN"
    
    while True:
        if len(path[current]) == 0 or not current in path:
            break
        
        ticket = path[current].pop(0)
        answer.append(ticket[0])
        current = ticket[1]
    
    answer.append(current)
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# 스택에 쌓고 다음 갈 경로 쌓기.
# 