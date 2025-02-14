from collections import deque

N = int(input())
cases = list()
for i in range(N):
    tmp = list()
    for i in range(3):
        if i == 0:
            tmp.append(input())
        elif i == 1:
            tmp.append(int(input()))
        else:
            arr = input()[1:-1]
            if len(arr) == 0:
                tmp.append([])
            else:
                tmp.append(deque(list(map(int,arr.split(',')))))
    cases.append(tmp)

for case in cases:
    # D가 배열 길이보다 길면 에러 출력하기
    if case[0].count('D') > case[1]:
        print('error')
        continue

    is_reversed = False
    for i in case[0]:
        
        if i == "D":
            if is_reversed:
                case[2].pop()
            else:
                case[2].popleft()
        else:
            is_reversed = not is_reversed

    # R 개수 구하기
    if is_reversed:
        case[2] = deque(reversed(case[2]))
    print("[" + ",".join(list(map(str,list(case[2])))) + "]")