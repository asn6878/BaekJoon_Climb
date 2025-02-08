from collections import deque

def solution(n, m, board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    Q = deque()
    Q.append([0,0])

    while Q:
        current = Q.popleft()
        x = current[0]
        y = current[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < n and nx >= 0 and ny < m and ny >= 0:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    Q.append([nx, ny])
                    board[nx][ny] = board[x][y] + 1
                    visited[nx][ny] = True

    print(board[n-1][m-1])


N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
solution(N, M, board)