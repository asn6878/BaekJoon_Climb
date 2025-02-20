import sys
input = sys.stdin.readline
N = int(input())
values = [int(input()) for _ in range(N)]
max_num = max(values)
dp = [0] * max_num
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, max_num):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for i in values:
    print(dp[i-1])
