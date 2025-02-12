import sys
from collections import deque
input = sys.stdin.readline

def solution():
    ps = input()
    s = deque()
    for i in ps:
        if i == '(':
            s.append(i)
        elif i == ')':
            if len(s) == 0:
                print("NO")
                return
            else:
                s.pop()
    
    if len(s) == 0:
        print('YES')
    else:
        print('NO')

N = int(input())
for _ in range(N):
    solution()