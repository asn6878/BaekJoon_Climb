n = int(input())
point = list()
bitmap = [[0 for i in range(100)] for j in range(100)]
for _ in range(n):
    square = list(map(int,input().split()))
    for i in range(10):
        for j in range(10):
            bitmap[square[0]+i][square[1]+j] = 1

answer = 0
for i in bitmap:
    for j in i:
        if j == 1:
            answer += 1

print(answer)