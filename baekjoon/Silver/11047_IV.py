N, K = map(int,input().split())
li = list()
quotinent = 0

for i in range(N):
    val = int(input())
    li.append(val)

for i in li[::-1]:
    if K != 0:            
        tmp = K // i
        quotinent += tmp
        K %= i
    else :
        break

print(quotinent)