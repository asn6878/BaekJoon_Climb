# 입력 받는 부분
width = int(input())
map_array = [list(map(int, input())) for _ in range(width)]

count = 0
answer = []
search_site = [[1,0],[-1,0],[0,1],[0,-1]]

def dfs(array, start_x, start_y):
    global count
    if 0 <= start_x < width and 0 <= start_y < width:
        if array[start_x][start_y] == 1:
            array[start_x][start_y] = 0
            count += 1
            for x,y in search_site:
                dfs(array, start_x+x,start_y+y)
    return

for x in range(width) :
    for y in range(width) :
        if map_array[x][y] == 1:
            dfs(map_array, x, y)
            answer.append(count)
            count = 0
print(len(answer))
answer.sort()
for i in answer:
    print(i)