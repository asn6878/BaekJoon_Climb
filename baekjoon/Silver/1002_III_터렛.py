import math
case = int(input())

for i in range(case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리

    if distance == 0 and r1 == r2: # 두명의 위치가 같을때 = 무한대
        print(-1)
    elif distance == r1 + r2 or distance == abs(r1-r2): # 두명이 외접 or 내접할때
        print(1)
    elif abs(r1-r2) < distance < r1 + r2: # 두명의 거리가 내접보다는 크고 외접보다는 작을때
        print(2)
    else :
        print(0)