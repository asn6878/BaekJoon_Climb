word = input()
temp = ""
for i in word[::-1]:
    temp += i
if word == temp:
    print(1)
else:
    print(0)