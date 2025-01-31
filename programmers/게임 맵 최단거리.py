from collections import deque

def solution(maps):
    bfs(maps, 0, 0)
    
    answer = maps[len(maps) - 1][len(maps[0])-1]
    
    if answer == 1:
        return -1
    return answer
    
def bfs(maps, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    Q = deque()
    Q.append([x, y])

    while (not len(Q) == 0):
        current = Q.popleft()
        x = current[0]
        y = current[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                Q.append([nx, ny])



print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))