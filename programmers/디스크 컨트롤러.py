import heapq as hq

def solution(jobs):
    completed = list()
    jobs.sort(key = lambda x : x[0], reverse = True)
    jobs = [[job[1], job[0], i] for i, job in enumerate(jobs)]
    
    current_task = [0,0,0]
    
    wait_q = list()
    time = 0
    
    while jobs or wait_q or current_task[0] > 0:
        # 여기는 작업 새로 얹는 부분
        while jobs and jobs[-1][1] == time:
            wait_q.append(jobs.pop())
            
        if len(wait_q) == 0 and current_task[0] == 0:
            time += 1
            continue
        elif len(wait_q) > 1:
            hq.heapify(wait_q)    
        
        # 현재 작업중이니?
        if current_task[0] > 0:
            current_task[0] -= 1
            time += 1
            continue
            
        completed.append(time - current_task[1])
        current_task = hq.heappop(wait_q)
        current_task[0] -= 1
        time += 1
    
    completed.append(time - current_task[1])
    completed.pop(0)
    
    return sum(completed) // len(completed)
    
print(solution([[0, 3], [1, 9], [3, 5]]))


# 첫 태스크 아무것도 안했는데 completed 에 추가됨.

# 마지막 태스크 실행 안끝나고 끝남