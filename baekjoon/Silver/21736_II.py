import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
N, M = map(int, input().split())

board = []
start = 0
answer = 0

for i in range(N):
    line = list(input())
    board.append(line)

    for idx, elem in enumerate(line):
        if elem == "I":
            start = (i, idx)
    
q = deque()
visited = [[False] * M for _ in range(N)]
q.append(start)
x, y = start
visited[x][y] = True

while q:
    cx, cy = q.popleft()

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M and not visited[nx][ny] and board[nx][ny] != 'X':
            q.append((nx, ny))
            visited[nx][ny] = True
            if board[nx][ny] == 'P':
                answer += 1

if answer == 0: print('TT')
else: print(answer)