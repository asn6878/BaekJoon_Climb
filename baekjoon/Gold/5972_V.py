import sys, heapq
input = sys.stdin.readline
MAX_INT = sys.maxsize

N, M = list(map(int,input().split()))
board = [[] for _ in range(N)]

for _ in range(M):
    f, t, d = list(map(int,input().split()))
    board[f-1].append((t-1, d))
    board[t-1].append((f-1, d))

q = list()
dist = [MAX_INT] * N
dist[0] = 0
heapq.heappush(q, (0, dist[0]))

while q:
    c_pos, c_dist = heapq.heappop(q)
    if c_dist > dist[c_pos]:
        continue

    for n_pos, n_dist in board[c_pos]:
        dist_sum = c_dist + n_dist
        if dist_sum < dist[n_pos]:
            dist[n_pos] = dist_sum
            heapq.heappush(q, (n_pos, dist_sum))

print(dist[N-1])