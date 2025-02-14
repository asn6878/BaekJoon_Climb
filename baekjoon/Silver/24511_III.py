import sys
from collections import deque
input = sys.stdin.readline

L = int(input())
ds = list(map(int, input().split()))
ov = list(map(int, input().split()))
N = int(input())
inputs = list(map(int, input().split()))
answer = list()
Q = deque()

for idx, datas in enumerate(ds):
    if datas == 0: #큐
        Q.appendleft(str(ov[idx]))
    else:
        continue

for i in inputs:
    Q.append(str(i))
    answer.append(Q.popleft())
    
print(" ".join(answer))