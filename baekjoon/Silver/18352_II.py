import sys
import heapq

input = sys.stdin.readline
INF = 300001

N, M, K, X = list(map(int, input().split()))
maps = [[] for _ in range(N)]

for _ in range(M):
    f, t = list(map(int, input().split()))
    maps[f-1].append(t-1)

def dijkstra(maps, start):
    distances = [INF for _ in range(N)]
    distances[start-1] = 0
    q = list()
    heapq.heappush(q, [distances[start-1], start-1])

    while q:
        d, c = heapq.heappop(q)

        if distances[c] < d:
            continue
            
        for i in maps[c]:
            new_dis = d + 1
            if distances[i] > new_dis:
                distances[i] = new_dis
                heapq.heappush(q, [distances[i], i])
    
    return distances

answer = dijkstra(maps, X)
answers = list()
for idx, i in enumerate(answer):
    if i == K:
        answers.append(idx+1)

if len(answers) == 0:
    print(-1)
else:
    for i in answers:
        print(i)