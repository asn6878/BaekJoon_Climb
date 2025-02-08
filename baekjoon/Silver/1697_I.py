from collections import deque

N, K = map(int, input().split())

def bfs(start):
    Q = deque()
    visited = [0 for _ in range(100001)]
    visited[start] = 1
    Q.append(start)
    cnt = 0

    while True:
        start = Q.popleft()
        if start == K:
            break
        cnt += 1
        
        for i in (start + 1, start - 1, start * 2):
            if i >= 0 and i < 100001 and visited[i] == 0:
                Q.append(i)
                visited[i] = visited[start] + 1

    return visited[K] - 1

print(bfs(N))