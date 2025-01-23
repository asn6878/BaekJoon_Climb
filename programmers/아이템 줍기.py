from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    scaled_rect = []
    for rect in rectangle:
        scaled_rect.append([coord * 2 for coord in rect])
    characterX, characterY = characterX * 2, characterY * 2
    itemX, itemY = itemX * 2, itemY * 2

    maximum = max(map(max, scaled_rect)) + 1
    li = [[0 for _ in range(maximum + 1)] for _ in range(maximum + 1)]
    
    for rect in scaled_rect:
        x1, y1, x2, y2 = rect
        
        for x in range(x1, x2 + 1):
            if li[y1][x] != 2:
                li[y1][x] = 1
            if li[y2][x] != 2:
                li[y2][x] = 1
        for y in range(y1, y2 + 1):
            if li[y][x1] != 2:
                li[y][x1] = 1
            if li[y][x2] != 2:
                li[y][x2] = 1

        for y in range(y1 + 1, y2):
            for x in range(x1 + 1, x2):
                li[y][x] = 2

    for y in range(maximum + 1):
        for x in range(maximum + 1):
            if li[y][x] == 2:
                li[y][x] = 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = [[False for _ in range(maximum + 1)] for _ in range(maximum + 1)]

    q = deque()
    q.append((characterY, characterX, 0))
    visited[characterY][characterX] = True

    while q:
        current_y, current_x, dist = q.popleft()        
        if current_y == itemY and current_x == itemX:
            return dist // 2
        
        for i in range(4):
            ny = current_y + dy[i]
            nx = current_x + dx[i]
            
            if 0 <= ny <= maximum and 0 <= nx <= maximum:
                if li[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx, dist + 1))

# # 입력 예시
# rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
# characterX = 1
# characterY = 3
# itemX = 7  # 가정한 값
# itemY = 8  # 가정한 값

# # solution 함수 호출
# result = solution(rectangle, characterX, characterY, itemX, itemY)
# print(result)
