# 4344 평균은 넘겠지

caseNum = int(input())
answerList = []
for i in range(caseNum):
    myli = list(map(int,input().split()))
    sum = 0
    overAvg = 0
    #print(myli)
    for i in range(1,len(myli)):
        sum = sum + myli[i]
    avg = sum / myli[0]
    for i in range(1,len(myli)):
        if myli[i] > avg:
            overAvg = overAvg + 1
    answerList.append(round(overAvg / myli[0] * 100, 3))

for i in answerList:
    str(i)
    print(f'{i:.3f}'+"%")