stk = []

def size(stk):
    print(len(stk))

def isEmpty(stk):
    if size(stk) == 0:
        return 1
    else :
        return 0

def push(stk, value):
    stk.append(value)

def pop(stk):
    if isEmpty(stk) == 0:
        print(stk[-1])
        stk.pop(-1)
    else :
        print(-1)

def top(stk):
    if isEmpty(stk) == 0:
        print(stk[-1])
    else :
        print(-1)

operations = int(input())
for i in range(operations):
    opList = list(input().split())
    if len(opList) > 1 :
        push(stk, opList[1])
    else :
        if opList[0] == "pop" :
            pop(stk)
        elif opList[0] == "size" :
            size(stk)
        elif opList[0] == "empty" :
            isEmpty(stk)
        elif opList[0] == "top" :
            top(stk)