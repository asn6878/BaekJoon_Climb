import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().strip()) for _ in range(N)]

dh = [0, 0, 1, -1]
dw = [1, -1, 0, 0]

# 적록 색약 => R == G
# 일반 => OK

def dfs_counter(board, is_saekyak):
    visited = [[False] * len(board) for _ in range(len(board))]
    cnt = 0
    if is_saekyak:
        for hi, vs in enumerate(visited):
            for wi, v in enumerate(vs):
                if not v:            
                    cnt += 1
                    visited = dfs_saekyak(board, visited, [hi, wi])
        return cnt
    else:
        for hi, vs in enumerate(visited):
            for wi, v in enumerate(vs):
                if not v:            
                    cnt += 1
                    visited = dfs(board, visited, [hi, wi])
        return cnt

def dfs_saekyak(board, visited, start):
    stack = list()
    h, w = start
    c_color = board[h][w]
    if c_color == "R" or c_color == "G":
        c_color = "RG"
    stack.append(start)
    visited[h][w] = True

    while stack:
        ch, cw = stack.pop()
        for i in range(4):
            nh = ch + dh[i]
            nw = cw + dw[i]

            if nh >= 0 and nh < len(board) and nw >= 0 and nw < len(board):
                if not visited[nh][nw] and board[nh][nw] in c_color:
                    visited[nh][nw] = True
                    stack.append([nh, nw])

    return visited

def dfs(board, visited, start):
    stack = list()
    h, w = start
    c_color = board[h][w]
    stack.append(start)
    visited[h][w] = True

    while stack:
        ch, cw = stack.pop()
        for i in range(4):
            nh = ch + dh[i]
            nw = cw + dw[i]

            if nh >= 0 and nh < len(board) and nw >= 0 and nw < len(board):
                if not visited[nh][nw] and board[nh][nw] == c_color:
                    visited[nh][nw] = True
                    stack.append([nh, nw])

    return visited

print(dfs_counter(board, False), dfs_counter(board, True))