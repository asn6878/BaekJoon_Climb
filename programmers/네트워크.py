def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0
    
    for i in range(len(visited)):
        if not visited[i]:
            dfs(i, computers, visited)
            answer += 1
        
    return answer

def dfs(i, computers, visited):
    visited[i] = True
    
    for j in range(len(computers[i])):
        if computers[i][j] == 1 and not visited[j]:
            dfs(i, computers, visited)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))