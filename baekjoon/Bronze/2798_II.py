import itertools

A, B = map(int,input().split())
C = list(map(int,input().split()))

min = B - 1

# 가능한 모든 조합을 구한다
combs = list(itertools.combinations(C,3))
for j in combs:
    tmp = sum(j) # 3개 수의 합을 구하고
    subs = B - tmp # 목표값에서 뺀다
    if subs < min and subs >= 0 : # 목표값보다 작거나 같고, 전역 최솟값보다 작으면
        min = subs # 최솟값 업데이트
        if min == 0: # 만약 0을 찾으면
            print(B) # 목표값 바로 출력후 종료
            exit()

print(B - min)