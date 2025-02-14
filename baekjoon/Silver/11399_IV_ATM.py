N = int(input())
times = list(map(int, input().split()))

times.sort()
tmp = 0
answer = 0
for t in times:
    tmp += t
    answer += tmp

print(answer)