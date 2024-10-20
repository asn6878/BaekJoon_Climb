import sys
input = sys.stdin.readline

stack = list()
n = int(input())

for _ in range(n):
    n = input().strip()
    if(n == '0'):
        stack.pop(-1)
    else:
        stack.append(int(n))
if(len(stack) > 0):
    print(sum(stack))
else:
    print(0)