li = list(int(input()) for _ in range (9))

first, second = 0, 0
# 10명의 난쟁이중 8명의 경우의수 뽑기
total = sum(li)

for i in range(8):
    for j in range(i+1,9):
        if total - (li[i] + li[j]) == 100:
            first = li[i]
            second = li[j]
            break

li.remove(first)
li.remove(second)
for i in sorted(li):
    print(i)
