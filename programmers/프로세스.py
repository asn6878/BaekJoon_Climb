from collections import deque

def solution(priorities, location):
    answer = 0
    m = 0
    
    tmp = deque()
    result = list()
    for i in range(len(priorities)):
        tmp.append([priorities[i], i])
    
    while not len(result) == len(priorities):    
        for i in range(len(tmp)):
            if tmp[i][0] > m:
                m = tmp[i][0]
        
        if tmp[0][0] == m:
            t = tmp.popleft()
            result.append(t)
        else:
            t = tmp.popleft()
            tmp.append(t)
        
        m = 0
    
    for i in range(len(result)):
        if result[i][1] == location:
            return i + 1
        
print(solution([2, 1, 3, 2], 2))