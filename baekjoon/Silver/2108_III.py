import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

# 산술 평균
avg = sum(nums) / len(nums)

if avg >= 0:
    print(int(avg + 0.5))
else:
    print(int(avg - 0.5))

# 중앙 값
print(nums[(len(nums) // 2)])

# 최빈 값
most_dict = defaultdict(int)
for i in nums:
    most_dict[i] += 1
most = max(most_dict.values())
most_li = list()

for k, v in most_dict.items():
    if v == most:
        most_li.append(k)

if len(most_li) == 1:
    print(most_li[0])
else:
    print(most_li[1])

# 범위
print(max(nums) - min(nums))