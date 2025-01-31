test_case = int(input())
for _ in range(test_case):
    N = int(input())
    wears = dict()
    result = 1
    for _ in range(N):
        name, w_type = input().split()
        if w_type in wears:
            wears[w_type] += 1
        else :
            wears[w_type] = 2
    for i in wears.values():
        result *= i
    print(result-1)