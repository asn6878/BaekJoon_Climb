N = int(input())
values = [0] * 301
for i in range(1, N + 1):
    values[i] = (int(input()))

dp = [0] * 301
dp[1] = values[1]
dp[2] = values[1] + values[2]
dp[3] = max(values[1] + values[3], values[2] + values[3])

for i in range(4, N+1):
    dp[i] = max(values[i] + dp[i-3] + values[i-1], values[i] + dp[i-2])

print(dp[N])