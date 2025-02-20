import sys
input = sys.stdin.readline

N, M = list(map(int,input().split()))
board = list([] for _ in range(N))
visited = list(False for _ in range(N))
cnt = 0

for i in range(M):
    f, t = list(map(int,input().split()))
    board[f-1].append(t-1)
    board[t-1].append(f-1)

for i in range(N):
    if not visited[i]:
        visited[i] = True
        stack = board[i][:]
        if stack:
            while stack:
                to_visit = stack.pop()
                if not visited[to_visit]:
                    visited[to_visit] = True
                    stack.extend(board[to_visit])
                
        cnt += 1

print(cnt)