import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 10001
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4
dp[5] = 5

for i in range(6, 10001):
    dp[i] = dp[i-3] + dp[i-2] + 1 - dp[i-5]

for i in range(N):
    K = int(input())
    print(dp[K])