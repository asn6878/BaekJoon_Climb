# BFS
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
values = [list(map(int, input().split())) for _ in range(N)]

for val in values:
    f, t = val
    Q = deque()
    Q.append((f, ""))
    visited = [False] * 10000
    visited[f] = True
    
    # while True:
    #     c_num, full_com = Q.popleft()

    #     if c_num == t:
    #         print("".join(full_com))
    #         break
        
    #     # D
    #     new_num = c_num * 2 % 10000
    #     if not visited[new_num]:
    #         visited[new_num] = True
    #         Q.append((new_num, full_com + 'D'))
    
    #     # S
    #     new_num = 9999 if c_num == 0 else c_num - 1
    #     if not visited[new_num]:
    #         visited[new_num] = True
    #         Q.append((new_num, full_com + 'S'))

    #     # L
    #     new_num = (c_num % 1000) * 10 + c_num // 1000
    #     if not visited[new_num]:
    #         visited[new_num] = True
    #         Q.append((new_num, full_com + 'L'))
        
    #     # R
    #     new_num = (c_num % 10) * 1000 + c_num // 10
    #     if not visited[new_num]:
    #         visited[new_num] = True
    #         Q.append((new_num, full_com + 'R'))

    while True:
        c_num, full_com = Q.popleft()

        if c_num == t:
            print("".join(full_com))
            break

        for op in "DSLR":
            if op == "D":
                new_num = c_num * 2 % 10000
            elif op == "S":
                new_num = 9999 if c_num == 1 else c_num - 1
            elif op == "L":
                new_num = (c_num % 1000) * 10 + c_num // 1000
            elif op == "R":
                new_num = (c_num % 10) * 1000 + c_num // 10
            
            if not visited[new_num]:
                visited[new_num] = True

                Q.append((new_num, full_com + op))