N = int(input())
M = int(input())
networks = [[] for _ in range(N)]
visited = [False] * N

for i in range(M):
    f, t = list(map(int,input().split()))
    networks[f-1].append(t-1)
    networks[t-1].append(f-1)

stack = list()
stack.append(0)
visited[0] = True
cnt = 0

while stack:
    c = stack.pop()
    for i in networks[c]:
        if not visited[i]:
            cnt += 1
            visited[i] = True
            stack.append(i)

print(cnt)