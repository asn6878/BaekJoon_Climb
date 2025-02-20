from collections import deque
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
values = list(map(int, input().split()))
adds = deque(values.copy())
adds.appendleft(0)

for i in range(1,N+1):
    adds[i] += adds[i-1]
for i in range(M):
    f, t = list(map(int, input().split()))
    print(adds[t] - adds[f-1])