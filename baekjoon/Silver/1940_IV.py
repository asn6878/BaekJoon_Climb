resource_num = int(input())
target = int(input())
li = sorted(list(map(int,input().split())))

start, end= 0, (len(li)-1)
counter = 0

while start != end:
    temp = li[start] + li[end]
    if temp > target:
        end -= 1
    elif temp < target:
        start += 1
    else:
        start += 1
        counter += 1

print(counter)





# def solution(li,start,end,target,count):
#     if end == (len(li) - 1):
#         return count
#     if start != end:
#         temp = li[start] + li[end]
#         if temp < target:
#             return solution(li,start,end+1,target,count)
#         elif temp > target:
#             return solution(li,start+1,end,target,count)
#         else :
#             return solution(li,start+1,end,target,count+1)
#     return solution(li,start,end+1,target,count)




