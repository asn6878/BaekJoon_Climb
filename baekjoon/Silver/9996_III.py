N = int(input())
shape = input()
head, foot = "", ""
flag = 0

for i in shape:
    if i == "*":
        flag += 1
    else:
        if flag == 0:
            head += i
        else :
            foot += i

for i in range(N):
    word = input()
    # 이부분이 안보여서 고생함. 단어가 애초에 헤더,푸터를 더한값보다 짧은 단어면 그어떤 상황이더라도 조건을 만족하지 못한다. 무조건 NE. 
    if head == word[0:len(head)] and foot == word[-len(foot):] and len(word) >= (len(head) + len(foot)):
        print("DA")
    else:
        print("NE")