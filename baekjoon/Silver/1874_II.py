from collections import deque

def solution():
    result = list()
    N = int(input())
    values = list()
    for _ in range(N):
        values.append(int(input()))

    nums = deque(i for i in range(1, N+1))
    stack = list()
    current = 1

    for v in values:
        if not stack and nums:
            for _ in range(current, v+1):
                stack.append(nums.popleft())
                result.append('+')
                current += 1
            stack.pop()
            result.append('-')
            continue
        
        if stack[-1] == v:
            stack.pop()
            result.append('-')
        elif stack[-1] > v:
            print('NO')
            return
        elif stack[-1] < v:
            for _ in range(current, v+1):
                stack.append(nums.popleft())
                result.append('+')
                current += 1
            stack.pop()
            result.append('-')

    return result

answer = solution()
if answer:
    for i in answer:
        print(i)