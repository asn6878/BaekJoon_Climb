def solution(n, costs):
    u_set = set()
    for i in range(n):
        u_set.update({i})
    
    print(u_set)
    answer = 0
    sorted_costs = sorted(costs, key=lambda x: x[2])
    
    while len(u_set) == 1:
        for i in sorted_costs:
            # 여기서 각 원소들이 들어가있는 집합이 다른 집합인지 확인.
            # 다른 집합이면 union 처리 해버리기.
            if not i[0] in visited or not i[1] in visited:
                answer += i[2]
                visited.update([i[0], i[1]])
                print(visited)
                
    return answer

print(solution(4, 	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))