import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
answer = [[0] * N for _ in range(N)]
board = list()
for i in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    q = deque()
    q.append(i)
    while q:
        current = q.popleft()
        for j in range(N):
            if board[current][j] == 1 and answer[i][j] == 0:
                q.append(j)
                answer[i][j] = 1
for arr in answer:
    print(' '.join(list(map(str, arr))))