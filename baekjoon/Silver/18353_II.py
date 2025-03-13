import sys
input = sys.stdin.readline

N = int(input())
soldiers = list(map(int, input().split()))
soldiers.reverse()

dp = [1] * N

for i in range(1,N):
    tmp = [0]
    for j in range(0, i):
        if soldiers[i] > soldiers[j]:
            tmp.append(dp[j])

    dp[i] = max(dp[i], max(tmp) + 1)

print(N - max(dp))