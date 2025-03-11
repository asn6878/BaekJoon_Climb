N, M, B = list(map(int, input().split()))
board = list()
for i in range(N):
    board.extend(list(map(int, input().split())))

answers = [0] * (257)

for height in range(257):
    to_mine = 0
    to_append = 0

    for j in board:
        if j > height:
            to_mine += j - height 
        elif j < height:
            to_append += height - j
        
    if B + to_mine - to_append < 0:
        answers[height] = -1
    else:
        answers[height] = (to_mine * 2) + (to_append)

a_height = 0
answer = answers[0]
for height, time in enumerate(answers):
    if not time == -1:
        if answer >= time:
            answer = time  
            a_height = height

print(answer, a_height)