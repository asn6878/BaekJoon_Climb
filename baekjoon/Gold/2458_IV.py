import sys
from collections import deque
input = sys.stdin.readline

# 모든 노드가 한번씩 출발점이 되어서 bfs 수행.
N, M = list(map(int, input().split()))
froms = [0] * N
tos = [0] * N
directions = [[] for _ in range(N)]

for i in range(M):
    f, t = list(map(int, input().split()))
    directions[f-1].append(t-1)

for start in range(N):
    # visited, 큐 초기화
    Q = deque()
    visited = [False] * N
    Q.append(start)
    froms[start] -= 1
    tos[start] -= 1
    # 첫 노드 방문
    while Q:
        current = Q.popleft()
        froms[current] += 1
        tos[start] += 1

        for to in directions[current]:
            if not visited[to]:
                Q.appendleft(to)
                visited[to] = True    

answer = 0
for i in range(N):
    if tos[i] + froms[i] == N - 1:
        answer += 1
print(answer)