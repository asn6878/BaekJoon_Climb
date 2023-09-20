K, N = map(int,input().split())
li = list(int(input()) for _ in range(K))

start, end = 1, max(li)
while start <= end:
    middle = (start + end) // 2
    lines = 0
    for i in li:
        lines += i // middle
    if lines >= N:
        start = middle + 1
    else:
        end = middle - 1

print(end)
        