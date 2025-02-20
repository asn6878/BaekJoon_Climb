import sys
input = sys.stdin.readline

def sol():    
    N, M = map(int, input().split())
    days = [[0] * M for _ in range(N)]
    for dessert in range(M):
        values = list(map(int, input().split()))
        for day in range(N):
            days[day][dessert] = values[day]
    
    if M == 1:
        answer = days[0][0]
        for i in range(1, N):
            answer += (days[i][0] // 2)
        
        return answer

    # dp[i][j] -> 0~i일까지 먹었을 때, i번째 날에 j번 디저트를 선택했을 때의 최대 누적 만족도.
    dp = [[0] * M for _ in range(N)]

    # 첫째날 (걍 그대로 넣기)
    for j in range(M):
        dp[0][j] = days[0][j]

    for i in range(1, N):
        for j in range(M):
            # 같은거 먹을때
            candidate_same = dp[i-1][j] + (days[i][j] // 2)
            # 다른거 먹을때
            candidate_diff = max(dp[i-1][k] for k in range(M) if k != j) + days[i][j]
            dp[i][j] = max(candidate_same, candidate_diff)

    return max(dp[N-1])

print(sol())