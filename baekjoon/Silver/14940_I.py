from collections import deque

def solution():
    H, W = list(map(int, input().split()))
    board = [list(map(int,input().split())) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if board[i][j] == 2:
                start = [i, j]
                break

    Q = deque()
    visited = [[False] * W for _ in range(H)]
    Q.append(start)
    visited[start[0]][start[1]] = True
    board[start[0]][start[1]] = 0

    dh = [0, 0, -1, 1]
    dw = [1, -1, 0, 0]

    while Q:
        ch, cw = Q.popleft()
        
        for i in range(4):
            nh = ch + dh[i]
            nw = cw + dw[i]

            if nh >= 0 and nh < H and nw >= 0 and nw < W:
                if not visited[nh][nw] and not board[nh][nw] == 0:
                    Q.append([nh, nw])
                    visited[nh][nw] = True
                    board[nh][nw] += board[ch][cw]

    for i in range(H):
        for j in range(W):
            if visited[i][j] == False and board[i][j] == 1:
                board[i][j] = -1

    for i in board:
        print(" ".join(map(str, i)))

solution()