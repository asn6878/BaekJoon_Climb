import sys

input = sys.stdin.readline
values = list(map(int, input().split()))

def solution(values):
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            f = i * values[0] + j * values[1]
            if f == values[2]:
               s = i * values[3] + j * values[4]
               if s == values[5]:
                   return [i, j]
    
answer = solution(values)
print(answer[0], answer[1])