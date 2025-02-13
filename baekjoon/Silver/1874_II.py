from collections import deque

N = int(input())
values = list()
for _ in range(N):
    values.append(int(input()))

nums = deque(i for i in range(1, N+1))
stack = list()
tmp = 0

for v in values:
    if not stack:
        while tmp != v:
            tmp = nums.popleft()
            stack.append(tmp)
            print('+')
        stack.pop()
        print('-')

    elif v == N - len(nums) - 1:
        stack.pop()
        print('-')
    
    elif v > N - len(nums) - 1:
        while tmp != v:
            tmp = nums.popleft()
            stack.append(tmp)
            print('+')
        stack.pop()
        print('-')
    else:
        print('NOT')
        break

    

    



    
    


stack = list()

