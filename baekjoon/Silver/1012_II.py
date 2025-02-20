# dfs 돌리고 count up
N = int(input())
dh = [0, 0, 1, -1]
dw = [1, -1, 0, 0]

for i in range(N):
    W, H, K = list(map(int, input().split()))
    farm = [[0] * W for _ in range(H)]
    for i in range(K):
        w, h = list(map(int,input().split()))
        farm[h][w] = 1

    visited = [[False] * W for _ in range(H)]
    answer = 0

    for h in range(H):
        for w in range(W):
            if not visited[h][w] and farm[h][w] == 1:
                stack = list()
                stack.append((h, w))
                visited[h][w] = True

                while stack:
                    ch, cw = stack.pop()
                    for k in range(4):
                        th = ch + dh[k]
                        tw = cw + dw[k]

                        if th >= 0 and th < H and tw >= 0 and tw < W and not visited[th][tw] and farm[th][tw] == 1:
                            visited[th][tw] = True
                            stack.append((th, tw))

                answer += 1
    print(answer)