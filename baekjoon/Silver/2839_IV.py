# 5로 나눠서 나오는 몫 (예를들어 17이면 0~3 까지 가능.)
def solution(N): 
    quotinent = N // 5
    answers = list()
    for i in range(0, quotinent + 1):
        remainder = N - 5 * i
        if remainder % 3 == 0:
            answers.append([i, remainder // 3])

    if len(answers) == 0:
        print(-1)
    else:
        print(sum(answers[-1]))

N = int(input())
solution(N)