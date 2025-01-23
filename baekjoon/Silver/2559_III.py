A, B = map(int,input().split())
li = list(map(int,input().split()))
result = sum(li[0:B])
temp = result

for i in range(B, len(li)):

    temp = temp - li[i-B] + li[i]
    if temp > result:
        result=temp
print(result)