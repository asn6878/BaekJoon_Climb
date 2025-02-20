import sys
input = sys.stdin.readline
N, H, W = list(map(int, input().split()))

def r(N, H, W):
    if N == 0:
        return 0

    half = 2 ** (N-1)
    q_size = half * half

    # 1사분면
    if H < half and W < half:
        return r(N-1, H, W)
    # 2사분면
    elif H < half and W >= half:
        return q_size + r(N - 1, H, W - half)
    # 3사분면
    elif H >= half and W < half:
        return 2 * q_size + r(N - 1, H - half, W)
    # 4사분면
    else:
        return 3 * q_size + r(N - 1, H - half, W - half)
    
print(r(N, H, W))