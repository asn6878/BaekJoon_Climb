import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
schedule = list()
max_profit = 0

for i in range(N):
    schedule.append(list(map(int, input().split())))

for i in range(N-1, -1, -1):
    time, profit = schedule[i]

    if time + i - 1 < N:
        dp[i] = max(profit + dp[i+time], max_profit)
        max_profit = dp[i]
    else:
        dp[i] = max_profit    

print(max_profit)