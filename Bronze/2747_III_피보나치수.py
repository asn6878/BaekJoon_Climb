a = int(input())

"""
# 재귀
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2)+fib(n-1)
"""

# DP
def fib(n):
    li = [None] * (n+1)
    li[0] = 0
    li[1] = 1
    for i in range(2,n+1):
        li[i] = li[i-1] + li[i-2]
    return li[n]

answer = fib(a)
print(answer)