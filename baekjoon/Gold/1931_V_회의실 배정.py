import sys

t = int(sys.stdin.readline())
values = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]

answer = 0
end_time = 0
values.sort(key = lambda x : (x[1], x[0]))

for start, end in values:
    if start >= end_time:
        answer += 1
        end_time = end

print(answer)