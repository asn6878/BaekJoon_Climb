# 힙 두개 사용 (음수 치환을 사용한 최대 힙 운용)
# 값 삭제시 -> heappop() 해보고 해당 힙 종류의 deleted_data 배열에 해당 값이 있으면 반복 수행
# 없으면 완료

# 최대값 삭제시 -> 쵀대 힙에서 heappop() 후 min_to_delete_data 배열에 역수 취해서 해당 값 추가
# 최소값 삭제시 => 최소 힙에서 heappop() 후 max_deleted_data 배열에 역수 취해서 해당 값 추가 

import heapq, sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    M = int(input())
    heap, m_heap = list(), list()
    min_to_delete, max_to_delete = list(), list()

    for i in range(M):
        com, num = input().strip().split()
        num = int(num)
        if com == 'I':
            # 추가 연산
            heapq.heappush(heap, num)
            heapq.heappush(m_heap, num * -1)

        else:
            if num == 1:
                if len(m_heap) - len(max_to_delete) <= 0: continue
                else:
                    while True:
                        popped = heapq.heappop(m_heap)
                        if popped in max_to_delete:
                            max_to_delete.remove(popped)
                            continue
                        min_to_delete.append(popped * -1) 
                        break

            else:
                if len(heap) - len(min_to_delete) <= 0: continue
                else:
                    while True:
                        popped = heapq.heappop(heap)
                        if popped in min_to_delete:
                            min_to_delete.remove(popped)
                            continue
                        max_to_delete.append(popped * -1)
                        break

    if len(heap) - len(min_to_delete) == 0:
        print('EMPTY')
        continue

    max_a = 0
    min_a = 0
    while not len(heap) - len(min_to_delete) == 0:
        popped = heapq.heappop(heap)
        if popped in min_to_delete:
            min_to_delete.remove(popped)
            continue
        min_a = popped
        break

    while not len(m_heap) - len(max_to_delete) == 0:
        popped = heapq.heappop(m_heap)
        if popped in max_to_delete:
            max_to_delete.remove(popped)
            continue
        max_a = popped * -1
        break

    print(max_a, min_a)