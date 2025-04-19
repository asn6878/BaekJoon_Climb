# 더 작은놈 / abs(Y - X) * 더 큰놈 == 최고 해
# X랑 Y 중 둘중 최고 해와 더 가까운 수를 최고해로 만들고
# 몇이나 차이나는지 확인
# 차이나는 수 * Y

import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    M, N, x, y = list(map(int, input().split()))
    answer = -1

    a = M if M > N else N
    b = x if a == M else y
    d = b

    while d <= M * N:
        if (d-x) % M == 0 and (d-y) % M == 0:
            answer = d
            break
        
        d += a
    print(answer)