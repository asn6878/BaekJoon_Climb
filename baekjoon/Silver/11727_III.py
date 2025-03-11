import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3
dp[3] = 5

def sol(n):
    global dp
    for i in range(4, n+1):
        dp[i] = dp[i-2] * 2 + dp[i-1]

sol(N)
print(dp[N] % 10007)