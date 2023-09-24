A, B = map(int,input().split())
li = list(map(int,input().split()))
S = sum(li[0:B])
print(S)

start, end = 0, B-1

for i in range(A-end):
    if end < len(li)-1:
        temp = S - li[start] + li[end+1]
        if temp > S:
            S = temp
        start += 1
        end += 1

print(S)