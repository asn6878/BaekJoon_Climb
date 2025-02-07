import sys, heapq

input = sys.stdin.readline

c = int(input())
values = list(int(input()) for _ in range(c))
reversed_values = map(lambda x: x * -1, values)

answer = list()
for i in reversed_values:
    if i == 0:
        if answer:
            print(heapq.heappop(answer) * -1)
        else:
            print(0)
    else:
        heapq.heappush(answer, i)