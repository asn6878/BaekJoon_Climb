A = int(input())

# 부분합 구하기
for i in range(1, A+1):
    string = str(i)
    result = 0
    li = list()
    for j in string:
        li.append(j)
    
    for k in li:
        num = int(k)
        result += num

    #부분합 + i가 A와 같다면 생성자임
    if (result + i) == A:
        print(i)
        exit()

print(0)