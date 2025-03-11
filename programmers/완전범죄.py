def solution(info, n, m):
    # dp[i][a][b] 가 True이면 i 개까지 물건을 훔쳤을 때 A도둑이 a만큼의 누적흔적을 가지고 B도둑이 b만큼의 누적 흔적을 가지는 것이 가능하다는 뜻임.
    dp = [[[False] * m for _ in range(n)] for _ in range(len(info) + 1)]
    
    
    # 0개의 물건까지 처리 했을때 A도둑과 B 도둑의 누적 흔적 값은 각각 0임. (무조건 가능)
    dp[0][0][0] = True
    
    for i, (info_a, info_b) in enumerate(info):
        for A in range(n):
            for B in range(m):
                # 가능한 상황 발견 시 거기서
                if dp[i][A][B]:
                    # A 도둑이 훔치는 경우
                    na = A + info_a
                    nb = B + info_b
                    if na < n:
                        dp[i+1][na][B] = True
                
                    # B 도둑이 훔치는 경우
                    if nb < m:
                        dp[i+1][A][nb] = True
    
    print(dp)
    
    for a in range(n):
        for b in range(m):
            if dp[len(info)][a][b]:
                return a
    
    return -1


# 아래는 예시 테스트 케이스입니다.
if __name__ == "__main__":
    print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))  # 기대값: 2
    # print(solution([[1, 2], [2, 3], [2, 1]], 1, 7))  # 기대값: 0
    # print(solution([[3, 3], [3, 3]], 7, 2))          # 기대값: 6
    # print(solution([[3, 3], [3, 3]], 6, 1))          # 기대값: -1
