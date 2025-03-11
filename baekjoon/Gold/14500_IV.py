H, W = list(map(int, input().split()))
board = list()
for i in range(H):
    board.append(list(map(int, input().split())))
visited = [[False] * W for _ in range(H)]

answer = 0
dw = [1, -1, 0, 0]
dh = [0, 0, 1, -1]

def dfs(w, h, cnt, tsum):
    global answer

    if cnt == 4:
        answer = max(answer, tsum)
        return
    for i in range(4):
        cw = w + dw[i]
        ch = h + dh[i]
        if cw >= 0 and cw < W and ch >= 0 and ch < H and not visited[ch][cw]:
            visited[ch][cw] = True
            dfs(cw, ch, cnt+1, tsum+board[ch][cw])
            visited[ch][cw] = False

def bubkyu(w, h):
    global answer

    tmp = list()
    for i in range(4):
        cw = w + dw[i]
        ch = h + dh[i]

        if cw >= 0 and cw < W and ch >= 0 and ch < H:
            tmp.append(board[ch][cw])

    if len(tmp) >= 3:
        if len(tmp) == 4:
            tmin = min(tmp)
            tmp.remove(tmin)
        answer = max(answer, sum(tmp) + board[h][w]) 

for h in range(H):
    for w in range(W):
        visited[h][w] = True
        dfs(w, h, 1, board[h][w])
        bubkyu(w, h)
        visited[h][w] = False

print(answer)