import sys, heapq

input = sys.stdin.readline

c = int(input())
values = list(int(input()) for _ in range(c))

answer = list()
for i in values:
    if i == 0:
        if answer:
            print(heapq.heappop(answer))
        else:
            print(0)
    else:
        heapq.heappush(answer, i)