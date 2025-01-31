li = list(0 for _ in range(26))

N = int(input())
for _ in range(N):
    i = input()
    li[ord(i[0])-97] += 1

answer = ""
for i in range(len(li)):
    if li[i] >= 5:
        answer += chr(i+97)

if len(answer) >= 1:
    print(answer)
else :
    print("PREDAJA")