A,B,C = map(int,input().split())
li = list(0 for _ in range(100))
for _ in range(3):
    start, end = map(int,input().split())
    # 카운팅 배열
    for i in range(start,end):
        li[i] += 1
        
for i in range(len(li)):
    if li[i] == 1:
        li[i] = A
    elif li[i] == 2:
        li[i] = B*2
    elif li[i] == 3:
        li[i] = C*3
print(sum(li))