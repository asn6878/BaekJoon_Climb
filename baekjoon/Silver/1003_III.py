N = int(input())
values = [int(input()) for _ in range(N)]

for i in values:
    a, b = [1, 0]
    for k in range(i):
        a, b = b, a+b
    print(a, b)