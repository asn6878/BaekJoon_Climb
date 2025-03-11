N = int(input())

dp = [0] * 101

values = list()
for i in range(N):
    values.append(int(input()))

target = max(values)
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, target+1):
    dp[i] = dp[i-3] + dp[i-2]

for i in values:
    print(dp[i])