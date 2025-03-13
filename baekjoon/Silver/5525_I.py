import sys
input = sys.stdin.readline

N = int(input())
length = int(input())
S = input().strip()

i, cnt, answer = 0, 0, 0

while i + 2 < length:
    if S[i:i+3] == 'IOI':
        cnt += 1
        if cnt == N:
            answer += 1
            cnt -= 1
        i += 2
    else:
        i += 1
        cnt = 0

print(answer)