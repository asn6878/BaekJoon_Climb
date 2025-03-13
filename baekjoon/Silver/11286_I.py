import heapq, sys
input = sys.stdin.readline

N = int(input())
nums = list()

for i in range(N):
    nums.append(int(input()))

heap = list()
m_heap = list()

for n in nums:
    if n == 0:
        if not heap and not m_heap:
            print(0)
            continue
        elif not heap: 
            print(heapq.heappop(m_heap) * -1)
            continue
        elif not m_heap: 
            print(heapq.heappop(heap))
            continue

        if heap[0] == m_heap[0]: print(heapq.heappop(m_heap) * -1)
        else:
            if heap[0] < m_heap[0]: print(heapq.heappop(heap))
            else: print(heapq.heappop(m_heap) * -1)

    else:
        if n > 0: heapq.heappush(heap, n)
        else: heapq.heappush(m_heap, abs(n))