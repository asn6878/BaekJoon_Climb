# 2738 행렬 덧셈

a, b = map(int,input().split()) 
li1, li2 = [], []

for i in range(a):
    t = list(map(int,input().split()))
    li1.append(t)
for i in range(a):
    t = list(map(int,input().split()))
    li2.append(t)
    
for i in range(a):
    for j in range(b):
        print(li1[i][j] + li2[i][j], end=' ')