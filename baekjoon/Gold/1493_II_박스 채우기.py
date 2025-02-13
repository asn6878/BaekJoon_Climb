X, Y, Z = list(map(int,input().split()))
N = int(input())
cubes = [list(map(int, input().split())) for _ in range(N)]

used_volume = 0
answer_cnt = 0
for i in range(len(cubes)-1, -1, -1):

    if used_volume >= (X * Y * Z):
        break

    size = 2 ** cubes[i][0]

    # 최대 갯수 구하기
    max_count = (X // size) * (Y // size) * (Z // size)
    max_count -= used_volume // (size ** 3)
    result_count = min(max_count, cubes[i][1])

    used_volume += result_count * (size ** 3)
    answer_cnt += result_count
    
if used_volume == (X * Y * Z):
    print(answer_cnt)
else:
    print(-1)