sentence = input()
answer = ""

for i in sentence:
    if i.isalpha():
        if i.isupper():
            N = ((ord(i) - 65) + 13) % 26
            answer+= chr(N+65)
        else:
            N = ((ord(i) - 97) + 13) % 26
            answer+= chr(N+97)
    else:
        answer+= i

print(answer)