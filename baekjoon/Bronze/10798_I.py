import sys
input = sys.stdin.readline

li, length = list(), list()

for _ in range(5):
    word = input().strip()
    li.append(word)
    length.append(len(word))

for i in range(max(length)):
    for j in range(len(li)):
        try:
            print(li[j][i], end="")
        except:
            continue