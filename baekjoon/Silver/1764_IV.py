import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))

nl = [input().strip() for _ in range(N)]
ns = [input().strip() for _ in range(M)]

nl_set = set(nl)
ns_set = set(ns)

all_set = nl_set & ns_set

print(len(all_set))

sorted_all = sorted(list(all_set))
for i in sorted_all:
    print(i)