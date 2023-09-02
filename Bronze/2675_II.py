import sys
input = sys.stdin.readline
num = int(input())

for i in range(num):
    N, M = input().split()
    for j in M:
        print(j*int(N), end="")
    print()