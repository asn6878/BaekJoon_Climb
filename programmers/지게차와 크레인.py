from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
takable = set()

def solution(storage, requests):
    containers = [[] for _ in range(len(storage))]
    for idx, items in enumerate(storage):
        for item in items:
            containers[idx].append(item)
    
    for req in requests:
        type = len(req)
        
        if type == 1:
            take = list()
            for i in range(len(containers)):
                for j in range(len(containers[i])):
                    if containers[i][j] == req[0]:
                        if (i,j) in takable:
                            take.append((i,j))
                            continue
                        if is_takable(containers, (i, j)):
                            take.append((i,j))
                            
            for x, y in take:
                containers[x][y] = 0
                for k in range(4):
                    takable.add((x + dx[k], y + dy[k]))
            
        else:
            for i in range(len(containers)):
                for j in range(len(containers[i])):
                    if containers[i][j] == req[0]:
                        containers[i][j] = 0
    
    answer = 0
    for i in containers:
        for j in i:
            if not j == 0:
                answer += 1  
    return answer

def is_takable(containers, pos):
    x, y = pos
    if x == len(containers) - 1 or x == 0 or y == len(containers[0]) - 1 or y == 0:
            return True

    q = deque()
    visited = [[False] * len(containers[0]) for _ in range(len(containers))]
    
    q.append(pos)
    visited[x][y] = True
    
    while q:
        cx, cy = q.popleft()
        if cx == len(containers) - 1 or cx == 0 or cy == len(containers[0]) - 1 or cy == 0:
            return True
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if nx < len(containers) and nx >= 0 and ny < len(containers[0]) and ny >= 0:
                if containers[nx][ny] == 0:
                    q.append((nx, ny))        
    return False