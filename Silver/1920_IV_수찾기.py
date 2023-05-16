import sys
input = sys.stdin.readline

a_num = int(input())
a_list = set(map(int,input().split()))
b_num = int(input())
b_list = list(map(int,input().split()))
# a_list.sort() set쓰면 sorting안해도 됨.

for i in b_list:
    if i in a_list:
        print(1)
    else :
        print(0)