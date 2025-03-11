# 냅색 프로블럼
import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
stuffs = list()
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(N):
    weight, value = list(map(int, input().split()))
    stuffs.append((weight, value))

# 결국은 물건 하나씩 경우의 수 따져보는 수 밖에 없음
# dp[i][j] 는 물건 개수 i 개 만큼 담을 수 있고, j무게 만큼 까지 사용했을 때 최선의 가치를 의미함.

for i in range(1, N+1):
    for j in range(K+1):
        weight, value = stuffs[i-1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])

print(dp[N][K])