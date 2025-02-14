N = int(input())

target = 665
cnt = 0
while True:
    if '666' in str(target):
        cnt += 1
        if cnt == N:
            break
    
    target += 1

print(target)