from collections import deque

N = int(input())
commands = list()
stack = deque()

for _ in range(N):
    commands.append(input().split())

for c in commands:
    if c[0] == 'push':
        stack.append(int(c[1]))
    elif c[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif c[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
