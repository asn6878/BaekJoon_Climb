from collections import Counter

def solution(points, routes):
    # 로봇의 위치를 파악
    r_positions = [points[route[0] - 1].copy() for route in routes]
    
    count = 0
    count += get_collision(r_positions)
    
    while not is_finished(r_positions):
        for i in range(len(routes)):
            # 남은 경로가 없는 로봇은 무시
            if not routes[i]:
                r_positions[i] = [-1, -1]
                continue
            
            current_dest = points[routes[i][0] - 1]
            if r_positions[i] == current_dest:
                routes[i].pop(0)
                if not routes[i]:
                    r_positions[i] = [-1, -1]
                    continue
                if routes[i]:
                    current_dest = points[routes[i][0] - 1]
            
            # 목적지가 남은 로봇 이동
            if r_positions[i] != [-1, -1]:
                x_mov = current_dest[0] - r_positions[i][0]
                y_mov = current_dest[1] - r_positions[i][1]
                
                if x_mov != 0:
                    r_positions[i][0] += (x_mov // abs(x_mov))
                else:
                    r_positions[i][1] += (y_mov // abs(y_mov))
        
        count += get_collision(r_positions)
    
    return count

def get_collision(r_positions):
    # [-1, -1] 위치를 제외하고 카운트
    filtered_positions = [tuple(pos) for pos in r_positions if pos != [-1, -1]]
    collision_counts = Counter(filtered_positions)
    collisions = sum(1 for count in collision_counts.values() if count >= 2)
    return collisions

def is_finished(r_positions):
    return all(pos == [-1, -1] for pos in r_positions)

# 예제 사용
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
