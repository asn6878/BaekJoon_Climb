from collections import deque

N, M = list(map(int, input().split()))
maps = [list(map(int, input().split())) for _ in range(M)]

def solution(N, M, maps):
    Q = deque()
    visited = [[False] * N for _ in range(M)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 1:
                visited[i][j] = True
                Q.append([i, j])
    
    while Q:    
        current = Q.popleft()
        for i in range(4):
            cx = current[0] + dx[i]
            cy = current[1] + dy[i]
            if cx >=0 and cx < M and cy >= 0 and cy < N:
                if maps[cx][cy] == 0 and not visited[cx][cy]:
                    maps[cx][cy] = maps[current[0]][current[1]] + 1
                    Q.append([cx, cy])
                    visited[cx][cy] = True
    
    answer = 0
    for i in maps:
        print(i)
    
    for v in maps:
        if 0 in v:
            return -1
        if answer < max(v):
            answer = max(v)
        
    return answer - 1

print(solution(N, M, maps))