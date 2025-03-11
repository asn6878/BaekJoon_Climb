from collections import defaultdict
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
domain_dict = defaultdict(str)

targets = list()
for i in range(N):
    domain, password = input().strip('').split()
    domain_dict[domain] = password

for i in range(M):
    domain = input().strip()
    print(domain_dict[domain])