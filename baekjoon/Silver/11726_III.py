# 점화식 d[n] = d[n-2] + d[n-1]
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * N

def sol(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    
    dp[0] = 1
    dp[1] = 2
    for i in range(2,N):
        dp[i] = dp[i-2] + dp[i-1]

    return dp[N-1]
print(sol(N) % 10007)