import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

count = [0] * 10
distinct = 0
ans = 0
left = 0

for right in range(N):
    fruit = S[right]
    if count[fruit] == 0:
        distinct += 1
    count[fruit] += 1

    while distinct > 2:
        left_fruit = S[left]
        count[left_fruit] -= 1
        if count[left_fruit] == 0:
            distinct -= 1
        left += 1

    ans = max(ans, right - left + 1)

print(ans)