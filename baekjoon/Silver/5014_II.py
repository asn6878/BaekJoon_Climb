import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = list(map(int, input().split()))

q = deque()
visited = [False] * (F + 1)
counts = [-1] * (F + 1)

q.append(S)
visited[S] = True
counts[S] = 0

while q:
    c = q.popleft()
    if c == G:
        break

    c_up = c + U
    c_down = c - D

    if c_up <= F and not visited[c_up]:
        visited[c_up] = True
        counts[c_up] = counts[c] + 1
        q.append(c_up)
    
    if c_down > 0 and not visited[c_down]:
        visited[c_down] = True
        counts[c_down] = counts[c] + 1
        q.append(c_down)

if visited[G]:
    print(counts[G])
else:
    print('use the stairs')