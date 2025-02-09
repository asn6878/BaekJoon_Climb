sik = input()

answer = 0
for idx, n in enumerate(sik.split('-')):
    if idx == 0:
        answer += sum(list(map(int,n.split('+'))))
        continue

    if '+' in n:
        answer -= sum(list(map(int,n.split('+'))))
    else:
        answer -= int(n)

print(answer)