import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # int(1e9)는 10억

vertex, edge = map(int,input().split()) # 정점, 간선 수
s_node = int(input()) # 시작 노드
info = [[] for _ in range(vertex + 1)] # 모든 간선의 정보를 저장할 리스트
distance = [INF] * (vertex + 1) # 노드의 최단거리 테이블
queue = []

for i in range(edge): # 그래프의 정보를 입력 받는다.
    a, b, c = map(int,input().split()) # a -> b 하는데 드는비용이 c
    info[a].append([b, c])

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(queue, [0, start])

    while queue: # 큐가 빈 리스트가 될때까지 반복
        now_w, now_n = heapq.heappop(queue) # 현재 가중치 now_w, 현재 노드번호 now_n

        if distance[now_n] < now_w : # 현재 최단거리테이블에 있는 값이 새로 발견한 가중치보다 작으면 비교할필요가 없다.
            continue # 스킵
        
        for new_n, new_w in info[now_n]: # 현재 노드가 연결된 노드(new_n)들과 가중치(new_w) 들고옴. (새로운 노드)
            if distance[now_n] + new_w < distance[new_n]: # 만약 현재 노드를 거쳐서 새로운 노드로 가는 거리가 현재 최단거리 테이블에 있는값보다 작다면?
                distance[new_n] = distance[now_n] + new_w # 최단거리 테이블 정정
                heapq.heappush(queue, [distance[new_n], new_n])  # 힙에 넣는다. 이렇게 넣어놓으면 당장 가중치가 가장 적은것부터 꺼내어 위의 코드들을 반복한다.

dijkstra(s_node)

for i in distance[1:]:
    if i >= INF:
        print('INF')
    else:
        print(i)