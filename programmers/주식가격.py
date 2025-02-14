def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        tmp = []
        for j in range(i, len(prices) - 1):
            if prices[i] <= prices[j]:
                tmp.append(j)
            else:
                break
            
        answer.append(len(tmp))
        
    return answer

solution([1,2,3,2,3])