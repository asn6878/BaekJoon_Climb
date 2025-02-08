from collections import deque

X, Y, H= list(map(int, input().split()))
maps = [[list(map(int, input().split())) for _ in range(Y)] for _ in range(H)]

def solution(X, Y, H, maps):
    Q = deque()
    visited = [[[False] * X for _ in range(Y)] for _ in range(H)]
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    for h in range(H):
        for y in range(Y):
            for x in range(X):
                if maps[h][y][x] == 1:
                    visited[h][y][x] = True
                    Q.append([h, y, x])
    
    while Q:    
        current = Q.popleft()
        for i in range(6):
            cx = current[2] + dx[i]
            cy = current[1] + dy[i]
            cz = current[0] + dz[i]
            if cx >=0 and cx < X and cy >= 0 and cy < Y and cz >= 0 and cz < H:
                if maps[cz][cy][cx] == 0 and not visited[cz][cy][cx]:
                    maps[cz][cy][cx] = maps[current[0]][current[1]][current[2]] + 1
                    Q.append([cz, cy, cx])
                    visited[cz][cy][cx] = True

    answer = 0
    for i in maps:
        for j in i:
            if 0 in j:
                return -1
            if answer < max(j):
                answer = max(j)
    return answer - 1

print(solution(X, Y, H, maps))