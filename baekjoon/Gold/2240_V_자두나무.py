import sys
t, w = map(int, sys.stdin.readline().split())

arr = [0]
for _ in range(t):
    arr.append(int(sys.stdin.readline().strip()))

dp = [[0] * (w + 1) for _ in range(t + 1)]

for i in range(1, t + 1):

    if arr[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]

    for j in range(1, w + 1):
        if arr[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        elif arr[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[t]))
