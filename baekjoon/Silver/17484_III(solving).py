import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

if N == 1:
    print(min(board[0]))
    exit()

INF = float('inf')
dp = [[[INF] * 3 for _ in range(M)] for _ in range(N)]

for j in range(M):
    if j >= 1:
        dp[1][j-1][0] = min(dp[1][j-1][0], board[0][j] + board[1][j-1])
    dp[1][j][1] = min(dp[1][j][1], board[0][j] + board[1][j])
    if j + 1 < M:
        dp[1][j+1][2] = min(dp[1][j+1][2], board[0][j] + board[1][j+1])

for i in range(2, N):
    for j in range(M):
        for prev_dir in range(3):
            if dp[i-1][j][prev_dir] == INF:
                continue
            for new_dir, new_j in [(0, j-1), (1, j), (2, j+1)]:
                if new_dir == prev_dir:
                    continue
                if 0 <= new_j < M:
                    dp[i][new_j][new_dir] = min(dp[i][new_j][new_dir], dp[i-1][j][prev_dir] + board[i][new_j])

result = INF
for j in range(M):
    for d in range(3):
        result = min(result, dp[N-1][j][d])

print(result)