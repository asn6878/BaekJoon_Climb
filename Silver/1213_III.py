import collections

name = sorted(input(),reverse=True)
alph_dict = collections.Counter(name)

odd_key = ""
cnt = 0
for k,v in alph_dict.items():
    if v % 2 == 1:
        odd_key = k
        alph_dict[k] -= 1
        cnt += 1
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()

for k,v in alph_dict.items():
    for i in range(v//2):
        odd_key = k + odd_key + k
print(odd_key)
