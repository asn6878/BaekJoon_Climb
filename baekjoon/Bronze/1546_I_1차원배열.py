#1546 평균

def findMax(li):
    high = 0
    for i in li:
        if i > high:
            high = i
    return high

a = int(input())
li = list(map(int,input().split()))
sum = 0
maxScore = findMax(li)

for i in range(a):
    li[i] = li[i]/maxScore*100 
for i in li:
    sum += i

print(sum/a)