import sys, heapq
input = sys.stdin.readline
MAX_INT = sys.maxsize

N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
queue = list()

for i in range(M):
    start, dest, cost = list(map(int, input().split()))
    graph[start-1].append((dest-1, cost))

start, dest = list(map(int, input().split()))

distances = [MAX_INT] * N
distances[start-1] = 0
heapq.heappush(queue, (start-1, distances[start-1]))

while queue:
    current_pos, current_distance = heapq.heappop(queue)

    if distances[current_pos] < current_distance:
        continue

    for pos, new_distance in graph[current_pos]:
        distance_sum = current_distance + new_distance

        if distance_sum < distances[pos]:
            distances[pos] = distance_sum
            heapq.heappush(queue, (pos, distance_sum))
            
print(distances[dest-1])