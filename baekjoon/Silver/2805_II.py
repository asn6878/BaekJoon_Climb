N, T = list(map(int, input().split()))
trees = list(map(int, input().split()))
trees.sort(reverse=True)

def get_woods(H):
    # 주어진 높이 H보다 큰 나무에 대해 (나무 높이 - H)를 합산
    return sum((tree - H) for tree in trees if tree > H)
low = 0
high = max(trees)
result = 0

while low <= high:
    mid = (low + high) // 2
    if get_woods(mid) >= T:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)