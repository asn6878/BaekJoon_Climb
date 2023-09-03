# def checker(text:str, li:list):
#     for i in li:
#         if text.find(i) != -1:
#             return i
#         else :
#             continue
#     return 0

# def transfer(text:str, cro_alph:list):
#     answer = 0
#     while checker(text, cro_alph):
#         n = text.find(checker(text, cro_alph))
#         if text[n:n+3] == "dz=":
#             text = text.replace(text[:n+3], "")
#             answer += 1
#         else:
#             text = text.replace(text[:n+2], "")
#             answer += 1
#     return answer + len(text)

# WRONG!!!!

cro_alph = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
for i in cro_alph:
    word = word.replace(i,"1")
print(len(word))