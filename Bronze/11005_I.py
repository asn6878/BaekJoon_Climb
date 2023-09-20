def dton(num:str):
    if int(num) < 10 :
        return num
    return chr(int(num) + 55)

def converter(n,x,result):
    quot = n // x
    result.append(n % x)
    if quot >= x:
        return converter(quot,x,result)
    else:
        result.append(quot)
        return result

n, x = map(int,input().split())
li = list()
li = converter(n,x,li)

for i in li[::-1]:
    print(dton(str(i)), end="")