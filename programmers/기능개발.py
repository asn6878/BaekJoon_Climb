def solution(progresses, speeds):
    idx = 0
    answer = []
    
    while idx < len(speeds):
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        releases = 0
        while idx < len(speeds):
            if progresses[idx] >= 100:
                idx+= 1
                releases+= 1
            else :
               break
        if releases > 0:
            answer.append(releases)
    return answer