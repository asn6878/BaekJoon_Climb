import sys
from collections import deque
input = sys.stdin.readline

lines = list()
while True:
    line = input()
    if line == '.\n':
        break
    lines.append(line)

def solution(line):
    s = deque()
    for a in line:
        if a == '(' or a == '[':
            s.append(a)
        elif a == ')':
            if len(s) != 0:
                tmp = s.pop()
                if tmp != '(':
                    print('no')
                    return
            else:
                print('no')
                return
        elif a == ']':
            if len(s) != 0:
                tmp = s.pop()
                if tmp != '[':
                    print('no')
                    return
            else:
                print('no')
                return
    
    if len(s) == 0:
        print('yes')
    else:
        print('no')

for line in lines:
    solution(line)