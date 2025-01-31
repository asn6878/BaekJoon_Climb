import sys
input = sys.stdin.readline

width = int(input())
li = [list(map(int,input().split())) for _ in range(width)]
white, blue = 0, 0

def paperMaker(x,y,N):
    global white, blue
    color = li[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if color != li[i][j]:
                paperMaker(x,y,N//2)
                paperMaker(x,y+N//2,N//2)
                paperMaker(x+N//2,y,N//2)
                paperMaker(x+N//2,y+N//2,N//2)
                return
    if color == 0:
        white += 1
    else :
        blue += 1

paperMaker(0,0,width)
print(white)
print(blue)