# alph_dict = {}
# for i in "abcdefghijklmnopqrstuvwxyz":
#     alph_dict[i] = -1

# word = input()
# for i in range(len(word)):
#     if alph_dict[word[i]] == -1:
#         alph_dict[word[i]] = i

# for key, val in alph_dict.items():
#     print(val, end=" ")

word = input()
li = list()

for i in range(97,123):
    li.append(chr(i))

for i in li:
    try:
        print(word.index(i), end=" ")
    except:
        print(-1, end=" ")