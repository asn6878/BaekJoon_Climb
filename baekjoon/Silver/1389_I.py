import sys
from collections import deque
input = sys.stdin.readline
read_ints = lambda : list(map(int, input().split()))

N, M = read_ints()
board = [[] for _ in range(N)]
bacon_cnt = list()

for i in range(M):
    a, b = read_ints()
    board[a-1].append(b-1)
    board[b-1].append(a-1)

for i in range(N):
    q = deque()
    visited = [0] * N
    visited[i] = 1
    q.append(i)

    while q:
        current = q.popleft()
        for f in board[current]:
            if visited[f] == 0:
                q.append(f)
                visited[f] = visited[current] + 1

    bacon_cnt.append(sum(visited) - N)

for idx, cnt in enumerate(bacon_cnt):
    if cnt == min(bacon_cnt):
        print(idx+1)
        break