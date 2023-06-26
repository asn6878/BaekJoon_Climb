t = int(input())
li = []
for i in range(t):
    a, b = map(int,input().split())
    li.append(a+b)

for i in range(1,len(li)+1):
    print(f'Case #{i}: {li[i-1]}')