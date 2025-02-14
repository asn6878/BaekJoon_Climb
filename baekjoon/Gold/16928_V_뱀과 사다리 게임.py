from collections import deque

L, S = list(map(int, input().split()))
l_from = list()
l_to = list()
s_from = list()
s_to = list()

for i in range(L):
    f, t = list(map(int, input().split()))
    l_from.append(f-1)
    l_to.append(t-1)

for i in range(S):
    f, t = list(map(int,input().split()))
    s_from.append(f-1)
    s_to.append(t-1)

board = [0 for _ in range(100)]
visited = [False for _ in range(100)]
Q = deque()
Q.append(0)
visited[0] = True
movements = [1,2,3,4,5,6]

while Q:
    current = Q.popleft()
    for i in range(6):
        np = current + movements[i]
        if np < 100:
            if np in l_from:
                dest = l_to[l_from.index(np)]
            elif np in s_from:
                dest = s_to[s_from.index(np)]
            else:
                dest = np
            
            if not visited[dest]:
                Q.append(dest)
                visited[dest] = True
                board[dest] = board[current] + 1

print(board[-1])