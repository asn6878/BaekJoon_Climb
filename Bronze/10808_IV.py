import sys

word = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
alph_dict = {}
for i in alpha:
    alph_dict[i] = 0

for i in word:
    alph_dict[i] += 1

for i in alph_dict.values():
    print(i, end=" ")