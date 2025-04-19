def solution(n, q, ans):
    q_sets = list()
    for i in q:
        q_sets.append(set(i))
    confirmed_set = set()
    
    for i in range(5):
        for j in range(i, 5):
            intersection = q_sets[i] & q_sets[j]
            t = ans[i] + ans[j]
            if t > 5:
                t -= 5
            else:
                t = 0
            
            # if len(intersection) <= min(ans[i], ans[j]) and not len(intersection) == 0:
            if len(intersection) <= t and not len(intersection) == 0:
                # print(f'교집합 발견! {i}번 집합 {q_sets[i]} {j}번 집합 {q_sets[j]}의 교집합 : {intersection}, ans[i] = {ans[i]}, ans[j] = {ans[j]}')
                confirmed_set.update(list(intersection))
    
    answer = 1
    print(confirmed_set)
    for i in range(5 - len(confirmed_set)):
        answer *= n - len(confirmed_set) - i
    return answer

print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))