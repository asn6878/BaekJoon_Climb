def checker(word:str):
    li = list()
    for i in word:
        if (len(li) == 0) or (li[-1] == i) or not i in li:
            li.append(i)
        else:
            return False
    return True

seq = int(input())
answer = 0
for i in range(seq):
    word = input()
    if checker(word):
        answer += 1
print(answer)