from collections import deque

def solution(bridge_length, weight, truck_weights):
    t = 0
    current = deque()
    while truck_weights or current:
        # 트럭 시간 증가 시키기
        for c in current:
            c[0] += 1

        # 다 지나간 트럭 내리기
        if current[0][0] >= bridge_length:
            current.popleft()

        # 트럭 적재 가능한지 확인하고 올리기
        if truck_weights and sum(w for _,w in current) + truck_weights[0] <= weight:
            new_truck = truck_weights.pop(0)
            current.append([0, new_truck])

        # 시간 증가
        t += 1

    return t

print(solution(2, 10, [7,4,5,6]))