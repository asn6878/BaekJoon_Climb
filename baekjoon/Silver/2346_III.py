from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
balloons = deque(enumerate(map(int, input().split()), 1))  # (풍선 번호, 종이 값) 형태로 저장

result = []

while balloons:
    index, move = balloons.popleft()
    result.append(index)

    if not balloons:
        break
    
    # 양수/음수 이동 처리
    if move > 0:
        balloons.rotate(-(move - 1))
    else:
        balloons.rotate(-move)

print(' '.join(map(str, result)))
