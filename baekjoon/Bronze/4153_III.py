inputs = list()
while True:
    t = list(map(int, input().split()))
    if (t[0] == 0):
        break
    else:
        inputs.append(t)

for i in inputs:
    i.sort()
    ab = i[0] ** 2 + i[1] ** 2
    c = i[2] ** 2

    if ab == c:
        print('right')
    else:
        print('wrong')